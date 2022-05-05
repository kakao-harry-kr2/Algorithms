import re

def solution(word, pages):
    word = word.lower()
    num_pages = len(pages)
    url2idx = dict()
    count = [0] * num_pages
    outgoings = [[] for _ in range(num_pages)]
    incomings = [[] for _ in range(num_pages)]
    links = []

    for idx in range(num_pages):
        p = pages[idx].lower()
        # 각 page의 url 찾기
        url = re.search(r'(<meta property.+content=")(https://.*)"/>', p).group(2)
        url2idx[url] = idx

        for w in re.findall('[a-z]+', p):
            if w == word:
                count[idx] += 1

        # 각 page의 외부 링크 확인
        ex_urls = re.findall(r'<a href="(https://\S*)">', p)
        for ex_url in ex_urls:
            links.append((idx, ex_url))

    for idx, destUrl in links:
        if destUrl in url2idx.keys():
            outgoings[idx].append(url2idx[destUrl])
            incomings[url2idx[destUrl]].append(idx)
        else:
            outgoings[idx].append(destUrl)

    matching_score = []
    for i in range(num_pages):
        score = count[i]
        for page in incomings[i]:
            score += count[page] / len(outgoings[page])
        
        matching_score.append(score)
    
    max_index = -1
    max_score = -1

    for idx, score in enumerate(matching_score):
        if score > max_score:
            max_score = score
            max_index = idx

    return max_index

pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution("Blind", pages))
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution("Muzi", pages))