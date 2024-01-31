import csv
import requests
from concurrent.futures import ThreadPoolExecutor


class Proxy:
    def __init__(self, ip, port, protocol):
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def test_connection(self):
        proxy = {self.protocol: f'{self.protocol}://{self.ip}:{self.port}'}
        try:
            response = requests.get('https://httpbin.org/ip', proxies=proxy, timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False


class ProxyTester:
    def __init__(self, csv_path, chunk_size=100):
        self.csv_path = 'proxy_db.csv'
        self.chunk_size = chunk_size

    def read_csv_in_chunks(self):
        with open(self.csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            chunk = []
            for row in reader:
                chunk.append(Proxy(row['ip'], row['port'], 'http'))
                if len(chunk) == self.chunk_size:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk

    def test_proxies(self, proxies):
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_proxy = {executor.submit(proxy.test_connection): proxy for proxy in proxies}
            results = {}
            for future in future_to_proxy:
                proxy = future_to_proxy[future]
                try:
                    results[proxy] = future.result()
                except Exception as exc:
                    results[proxy] = False
            return results

    def run_tests(self):
        good_proxies = []
        bad_proxies = []
        for chunk in self.read_csv_in_chunks():
            results = self.test_proxies(chunk)
            for proxy, status in results.items():
                if status:
                    good_proxies.append(proxy)
                else:
                    bad_proxies.append(proxy)
        return good_proxies, bad_proxies


# Main execution
if __name__ == '__main__':
    tester = ProxyTester('proxy_db.csv')
    good_proxies, bad_proxies = tester.run_tests()
    print('Good Proxies:')
    for proxy in good_proxies:
        print(f'{proxy.ip}:{proxy.port}')
    print('\nBad Proxies:')
    for proxy in bad_proxies:
        print(f'{proxy.ip}:{proxy.port}')
