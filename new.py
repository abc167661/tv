import asyncio
import aiohttp
import re
import datetime
import requests
import eventlet
import os
import time
import threading
from queue import Queue
eventlet.monkey_patch()


urls = [
"http://1.58.247.68:4001"
"http://122.159.48.86:8888"
"http://113.3.244.208:4022"
"http://113.9.171.236:1688"
"http://122.158.81.51:4022"
"http://122.159.31.148:7777"
"http://113.4.188.135:4001"
"http://113.5.210.107:4022"
"http://113.2.165.170:4022"
"http://113.2.165.172:4022"
"http://1.63.42.180:4022"
"http://113.2.163.65:4022"
"http://60.219.228.210:4000"
"http://1.188.139.136:4022"
"http://113.2.147.115:4022"
"http://113.2.147.114:4022"
"http://113.2.146.88:4022"
"http://1.188.138.242:4022"
"http://60.219.228.150:4001"
"http://60.219.228.150:4000"
"http://113.2.189.137:4022"
"http://113.2.189.136:4022"
"http://1.56.223.7:4022"
"http://1.57.227.135:4022"
"http://1.57.227.171:4022"
"http://1.57.227.166:4022"
"http://60.219.228.143:4000"
"http://221.206.38.66:4022"
"http://113.2.189.126:4022"
"http://1.62.113.192:4000"
"http://113.5.209.36:4022"
"http://1.62.99.189:4000"
"http://113.5.216.201:4022"
"http://113.3.247.133:4022"
"http://1.57.224.119:4022"
"http://1.58.209.45:4000"
"http://1.58.246.183:4000"
"http://1.58.254.238:4001"
"http://1.58.87.254:8886"
"http://1.58.246.172:4000"
"http://221.208.26.64:4000"
"http://1.58.243.42:4001"
"http://1.62.241.44:8886"
"http://1.58.246.238:4001"
"http://1.57.224.103:4022"
"http://1.63.62.238:4022"
"http://1.63.62.216:4022"
"http://218.8.87.96:4000"
"http://125.211.120.40:4000"
"http://1.58.225.128:8886"
"http://1.56.158.40:4022"
"http://113.5.214.120:4022"
"http://1.62.3.37:4001"
"http://1.62.3.37:4000"
"http://125.211.135.25:4001"
"http://221.206.45.150:4022"
"http://1.62.46.126:4001"
"http://1.56.158.152:4022"
"http://113.1.192.71:4022"
"http://113.4.191.67:8500"
"http://1.189.0.130:8886"
"http://1.62.49.148:4000"
"http://1.63.40.39:4022"
"http://113.4.188.103:4001"
"http://1.56.158.15:4022"
"http://113.2.146.78:4022"
"http://113.2.146.80:4022"
"http://60.14.229.209:4022"
"http://60.14.229.193:4022"
"http://1.56.220.132:4022"
"http://1.56.206.225:4022"
"http://113.1.195.152:4022"
"http://113.5.212.103:4022"
"http://113.5.213.238:4022"
"http://1.58.71.189:4000"
"http://1.56.158.73:4022"
"http://113.8.247.128:4022"
"http://113.8.247.213:4022"
"http://113.5.215.25:4022"
"http://113.8.247.216:4022"
"http://1.62.241.68:8886"
"http://113.8.245.81:4022"
"http://1.57.226.102:4022"
"http://1.57.226.101:4022"
"http://1.62.122.107:4000"
"http://113.2.163.227:4022"
"http://1.58.254.178:4000"
"http://1.58.114.70:8886"
"http://113.8.240.143:4022"
"http://1.62.122.107:4001"
"http://113.5.210.57:4022"
"http://1.58.246.199:4001"
"http://1.58.254.178:4001"
"http://1.58.246.199:4000"
"http://1.58.247.93:4000"
"http://1.62.112.55:8886"
"http://1.62.123.88:4001"
"http://1.62.130.222:4000"
"http://113.4.185.119:8500"
"http://113.4.231.179:4000"
"http://1.62.231.204:8886"
"http://113.3.244.135:4022"
"http://218.8.85.249:8500"
"http://221.206.39.174:4022"
"http://1.62.113.142:4000"
"http://221.207.174.111:4000"
"http://1.58.246.240:4000"
"http://221.211.11.90:4022"
"http://1.63.62.187:4022"
"http://113.9.99.109:4000"
"http://218.8.42.248:8500"
"http://113.8.243.26:4022"
"http://113.8.243.28:4022"
"http://221.210.252.76:4022"
"http://1.62.91.90:8886"
"http://1.56.158.119:4022"
"http://113.5.222.48:4022"
"http://218.7.89.61:4022"
"http://1.62.142.49:8886"
"http://1.57.224.28:4022"
"http://113.2.166.114:4022"
"http://1.56.252.79:4022"
"http://113.5.218.26:4022"
"http://218.8.75.23:8500"
"http://218.7.82.17:4022"
"http://1.58.243.169:4000"
"http://1.190.144.178:4000"
"http://1.58.246.118:4000"
"http://1.189.69.228:4000"
"http://218.8.42.128:8500"
"http://113.3.254.249:4022"
"http://60.219.186.32:4000"
"http://1.58.209.63:4001"
"http://1.63.60.214:4022"
"http://218.8.75.212:8886"
"http://1.58.209.63:4000"
"http://221.206.58.150:4022"
"http://122.158.159.55:4022"
"http://1.56.220.60:4022"
"http://221.206.58.48:4022"
"http://218.8.42.115:8500"
"http://221.206.54.128:4022"
"http://221.206.54.132:4022"
"http://113.9.235.109:4022"
"http://1.58.246.252:4000"
"http://1.62.130.83:4001"
"http://221.206.45.252:4022"
"http://113.8.244.104:4022"
"http://1.190.144.224:4001"
"http://113.8.245.126:4022"
"http://218.7.83.28:4022"
"http://113.8.245.2:4022"
"http://113.8.244.255:4022"
"http://122.159.47.48:8888"
"http://1.56.252.22:4022"
"http://1.189.69.107:4000"
"http://113.4.188.77:8500"
"http://113.0.92.197:4000"
"http://1.58.246.124:4000"
"http://122.159.57.60:8888"
"http://113.9.235.113:4022"
"http://1.58.243.57:4000"
"http://113.4.188.180:8500"
"http://113.9.235.82:4022"
"http://113.4.231.16:4000"
"http://1.62.123.69:4000"
"http://113.4.185.57:4000"
"http://1.56.253.86:4022"
"http://122.159.62.43:8888"
"http://1.62.99.91:4000"
"http://1.62.46.155:4000"
"http://218.7.82.216:4022"
"http://113.8.241.51:4022"
"http://113.9.235.93:4022"
"http://1.62.3.105:4000"
"http://122.159.61.205:8888"
"http://220.201.200.4:9000"
"http://1.58.247.185:4000"
"http://1.190.207.137:4000"
"http://113.4.227.45:8500"
"http://113.2.189.43:4022"
"http://1.58.254.196:4001"
"http://113.5.163.152:10010"
"http://221.208.26.150:4000"
"http://113.2.163.246:4022"
"http://220.201.200.142:9000"
"http://220.201.200.168:9000"
"http://1.190.144.86:4000"
"http://113.9.98.194:4001"
"http://113.9.235.217:4022"
"http://122.159.46.9:6666"
"http://1.58.247.227:4001"
"http://122.159.41.159:6666"
"http://220.201.200.100:9000"
"http://1.62.250.221:8886"
"http://113.2.162.226:4022"
"http://113.2.162.227:4022"
"http://113.2.162.225:4022"
"http://1.62.3.226:8001"
"http://221.206.39.85:4022"
"http://125.211.150.178:4000"
"http://220.201.200.134:9000"
"http://113.9.235.229:4022"
"http://1.62.3.226:5002"
"http://1.58.243.183:4000"
"http://1.62.3.226:5001"
"http://218.7.83.246:4022"
"http://113.2.162.237:4022"
"http://220.201.200.156:9000"
"http://220.201.200.155:9000"
"http://113.4.191.80:5002"
"http://1.62.112.116:8886"
"http://1.58.247.173:4000"
"http://1.63.60.208:4022"
"http://113.4.191.80:5001"
"http://113.4.168.252:4000"
"http://1.58.243.115:4000"
"http://113.2.161.116:4022"
"http://1.189.189.229:4000"
"http://1.188.140.205:4022"
"http://113.8.246.69:4022"
"http://1.188.141.235:4022"
"http://220.201.200.95:9000"
"http://220.201.200.111:9000"
"http://1.58.247.76:8500"
"http://218.9.253.251:4000"
"http://1.62.113.153:4000"
"http://221.209.212.57:4848"
"http://122.159.6.142:6666"
"http://1.62.3.226:5003"
"http://113.9.235.8:4022"
"http://1.62.3.47:8500"
"http://1.63.96.11:4848"
"http://1.62.83.31:8886"
"http://1.62.3.58:4000"
"http://1.63.62.74:4022"
"http://1.63.62.75:4022"
"http://113.3.253.180:4022"
"http://1.62.3.199:8001"
"http://220.201.200.250:9000"
"http://220.201.200.211:9000"
"http://113.5.163.197:10010"
"http://113.8.241.252:4022"
"http://113.8.241.226:4022"
"http://1.62.3.199:5003"
"http://113.0.58.7:4000"
"http://113.4.191.99:4000"
"http://113.0.58.7:4001"
"http://220.201.200.22:9000"
"http://113.9.98.221:4000"
"http://1.58.203.144:8886"
"http://221.206.38.201:4022"
"http://122.159.41.146:6666"
"http://113.0.58.5:4001"
"http://113.5.214.199:4022"
]


async def modify_urls(url):
    modified_urls = []
    ip_start_index = url.find("//") + 2
    ip_end_index = url.find(":", ip_start_index)
    base_url = url[:ip_start_index]
    ip_address = url[ip_start_index:ip_end_index]
    port = url[ip_end_index:]
    ip_end = "/iptv/live/1000.json?key=txiptv"
    for i in range(1, 256):
        modified_ip = f"{ip_address[:-1]}{i}"
        modified_url = f"{base_url}{modified_ip}{port}{ip_end}"
        modified_urls.append(modified_url)
    return modified_urls

async def is_url_accessible(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url, timeout=0.5) as response:
                if response.status == 200:
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{current_time} {url}")
                    return url
        except (aiohttp.ClientError, asyncio.TimeoutError):
            pass
    return None

async def check_urls(session, urls, semaphore):
    tasks = []
    for url in urls:
        url = url.strip()
        modified_urls = await modify_urls(url)
        for modified_url in modified_urls:
            task = asyncio.create_task(is_url_accessible(session, modified_url, semaphore))
            tasks.append(task)
    results = await asyncio.gather(*tasks)
    valid_urls = [result for result in results if result]
    return valid_urls

async def fetch_json(session, url, semaphore):
    async with semaphore:
        try:
            ip_start_index = url.find("//") + 2
            ip_dot_start = url.find(".") + 1
            ip_index_second = url.find("/", ip_dot_start)
            base_url = url[:ip_start_index]
            ip_address = url[ip_start_index:ip_index_second]
            url_x = f"{base_url}{ip_address}"

            json_url = f"{url}"
            async with session.get(json_url, timeout=0.5) as response:
                json_data = await response.json()
                results = []
                try:
                    for item in json_data['data']:
                        if isinstance(item, dict):
                            name = item.get('name')
                            urlx = item.get('url')
                            if ',' in urlx:
                                urlx = "aaaaaaaa"
                            if 'http' in urlx:
                                urld = f"{urlx}"
                            else:
                                urld = f"{url_x}{urlx}"

                            if name and urlx:
                                name = name.replace("cctv", "CCTV")
                                name = name.replace("中央", "CCTV")
                                name = name.replace("央视", "CCTV")
                                name = name.replace("高清", "")
                                name = name.replace("超高", "")
                                name = name.replace("HD", "")
                                name = name.replace("标清", "")
                                name = name.replace("频道", "")
                                name = name.replace("-", "")
                                name = name.replace(" ", "")
                                name = name.replace("PLUS", "+")
                                name = name.replace("＋", "+")
                                name = name.replace("(", "")
                                name = name.replace(")", "")
                                name = re.sub(r"CCTV(\d+)台", r"CCTV\1", name)
                                name = name.replace("CCTV1综合", "CCTV1")
                                name = name.replace("CCTV2财经", "CCTV2")
                                name = name.replace("CCTV3综艺", "CCTV3")
                                name = name.replace("CCTV4国际", "CCTV4")
                                name = name.replace("CCTV4中文国际", "CCTV4")
                                name = name.replace("CCTV4欧洲", "CCTV4")
                                name = name.replace("CCTV5体育", "CCTV5")
                                name = name.replace("CCTV6电影", "CCTV6")
                                name = name.replace("CCTV7军事", "CCTV7")
                                name = name.replace("CCTV7军农", "CCTV7")
                                name = name.replace("CCTV7农业", "CCTV7")
                                name = name.replace("CCTV7国防军事", "CCTV7")
                                name = name.replace("CCTV8电视剧", "CCTV8")
                                name = name.replace("CCTV9记录", "CCTV9")
                                name = name.replace("CCTV9纪录", "CCTV9")
                                name = name.replace("CCTV10科教", "CCTV10")
                                name = name.replace("CCTV11戏曲", "CCTV11")
                                name = name.replace("CCTV12社会与法", "CCTV12")
                                name = name.replace("CCTV13新闻", "CCTV13")
                                name = name.replace("CCTV新闻", "CCTV13")
                                name = name.replace("CCTV14少儿", "CCTV14")
                                name = name.replace("CCTV15音乐", "CCTV15")
                                name = name.replace("CCTV16奥林匹克", "CCTV16")
                                name = name.replace("CCTV17农业农村", "CCTV17")
                                name = name.replace("CCTV17农业", "CCTV17")
                                name = name.replace("CCTV5+体育赛视", "CCTV5+")
                                name = name.replace("CCTV5+体育赛事", "CCTV5+")
                                name = name.replace("CCTV5+体育", "CCTV5+")
                                results.append(f"{name},{urld}")
                except Exception:
                    pass
                return results
        except (aiohttp.ClientError, asyncio.TimeoutError, ValueError):
            return []

async def main():
    x_urls = []
    for url in urls:
        url = url.strip()
        ip_start_index = url.find("//") + 2
        ip_end_index = url.find(":", ip_start_index)
        ip_dot_start = url.find(".") + 1
        ip_dot_second = url.find(".", ip_dot_start) + 1
        ip_dot_three = url.find(".", ip_dot_second) + 1
        base_url = url[:ip_start_index]
        ip_address = url[ip_start_index:ip_dot_three]
        port = url[ip_end_index:]
        ip_end = "1"
        modified_ip = f"{ip_address}{ip_end}"
        x_url = f"{base_url}{modified_ip}{port}"
        x_urls.append(x_url)
    unique_urls = set(x_urls)

    semaphore = asyncio.Semaphore(500)
    async with aiohttp.ClientSession() as session:
        valid_urls = await check_urls(session, unique_urls, semaphore)
        all_results = []
        tasks = []
        for url in valid_urls:
            task = asyncio.create_task(fetch_json(session, url, semaphore))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        for sublist in results:
            all_results.extend(sublist)


    eventlet.monkey_patch()
    task_queue = eventlet.Queue()
    results = []
    error_channels = []

    def worker():
        while True:
            # 从队列中获取一个任务
            channel_name, channel_url = task_queue.get()
            try:
                channel_url_t = channel_url.rstrip(channel_url.split('/')[-1])  # m3u8链接前缀
                lines = requests.get(channel_url, timeout=1).text.strip().split('\n')  # 获取m3u8文件内容
                ts_lists = [line.split('/')[-1] for line in lines if line.startswith('#') == False]  # 获取m3u8文件下视频流后缀
                ts_lists_0 = ts_lists[0].rstrip(ts_lists[0].split('.ts')[-1])  # m3u8链接前缀
                ts_url = channel_url_t + ts_lists[0]  # 拼接单个视频片段下载链接

                # 多获取的视频数据进行5秒钟限制
                with eventlet.Timeout(5, False):
                    start_time = datetime.datetime.now().timestamp()
                    content = requests.get(ts_url, timeout=1).content
                    end_time = datetime.datetime.now().timestamp()
                    response_time = (end_time - start_time) * 1

                if content:
                    with open(ts_lists_0, 'ab') as f:
                        f.write(content)  # 写入文件
                    file_size = len(content)
                    # print(f"文件大小：{file_size} 字节")
                    download_speed = file_size / response_time / 1024
                    # print(f"下载速度：{download_speed:.3f} kB/s")
                    normalized_speed = min(max(download_speed / 1024, 0.001), 100)  # 将速率从kB/s转换为MB/s并限制在1~100之间
                    # print(f"标准化后的速率：{normalized_speed:.3f} MB/s")

                    # 删除下载的文件
                    os.remove(ts_lists_0)
                    result = channel_name, channel_url, f"{normalized_speed:.3f} MB/s"
                    results.append(result)
                    numberx = (len(results) + len(error_channels)) / len(all_results) * 100
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{current_time}可用频道：{len(results)} 个 , 不可用频道：{len(error_channels)} 个 , 总频道：{len(all_results)} 个 ,总进度：{numberx:.2f} %。")
            except:
                error_channel = channel_name, channel_url
                error_channels.append(error_channel)
                numberx = (len(results) + len(error_channels)) / len(all_results) * 100
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{current_time}可用频道：{len(results)} 个 , 不可用频道：{len(error_channels)} 个 , 总频道：{len(all_results)} 个 ,总进度：{numberx:.2f} %。")

            # 标记任务完成
            task_queue.task_done()

    def channel_key(channel_name):
        match = re.search(r'\d+', channel_name)
        if match:
            return int(match.group())
        else:
            return float('inf')



    # 创建工作线程
    num_workers = 10
    #pool = eventlet.GreenPool(num_workers)
    for _ in range(num_workers):
        #pool.spawn(worker)
        t = threading.Thread(target=worker, daemon=True)  # 将工作线程设置为守护线程
        t.start()


    # 将all_results中的数据放入任务队列
    for result in all_results:
        channel_name, channel_url = result.split(',')
        task_queue.put((channel_name, channel_url))


    # 等待所有任务完成
    task_queue.join()

    # 对结果进行排序
    #results.sort(key=lambda x: channel_key(x[0]))
    results.sort(key=lambda x: (x[0], -float(x[2].split()[0])))
    results.sort(key=lambda x: channel_key(x[0]))

    # 保存结果到文件
    with open("speed_results.txt", 'w', encoding='utf-8') as file:
        for result in results:
            file.write(f"{result[0]},{result[1]},{result[2]}\n")

    result_counter = 8  # 每个频道需要的个数

    with open("itvlist.txt", 'w', encoding='utf-8') as file:
        channel_counters = {}
        file.write('央视频道,#genre#\n')
        for result in results:
            channel_name, channel_url, speed = result
            if 'CCTV' in channel_name:
                if channel_name in channel_counters:
                    if channel_counters[channel_name] >= result_counter:
                        continue
                    else:
                        file.write(f"{channel_name},{channel_url}\n")
                        channel_counters[channel_name] += 1
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] = 1
        channel_counters = {}
        file.write('卫视频道,#genre#\n')
        for result in results:
            channel_name, channel_url, speed = result
            if '卫视' in channel_name:
                if channel_name in channel_counters:
                    if channel_counters[channel_name] >= result_counter:
                        continue
                    else:
                        file.write(f"{channel_name},{channel_url}\n")
                        channel_counters[channel_name] += 1
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] = 1
        channel_counters = {}
        file.write('其他频道,#genre#\n')
        for result in results:
            channel_name, channel_url, speed = result
            if 'CCTV' not in channel_name and '卫视' not in channel_name and '测试' not in channel_name:
                if channel_name in channel_counters:
                    if channel_counters[channel_name] >= result_counter:
                        continue
                    else:
                        file.write(f"{channel_name},{channel_url}\n")
                        channel_counters[channel_name] += 1
                else:
                    file.write(f"{channel_name},{channel_url}\n")
                    channel_counters[channel_name] = 1


if __name__ == "__main__":
    asyncio.run(main())
