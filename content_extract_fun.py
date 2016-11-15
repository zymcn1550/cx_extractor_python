from bs4 import BeautifulSoup
class content_extract:
#html = html code
    def __init__(self,html,depth=5,threshold=80):
        self.html = html
        self.depth = depth
        self.threshold = threshold
    def htmlcleaner(self):
        soup = BeautifulSoup(self.html, "html.parser")
        for script in soup.select("script"):
            script.extract()
        for style in soup.select("style"):
            style.extract()
        bsoup = soup.get_text().split("\n")
        return bsoup
    def contentextractor(self,text):
        block = ""
        cblock = []
        indexDistribution = []
        start = -1
        end = -1
        start_bool = False
        end_bool = False
        starts = {}
        for i in range(len(text)-self.depth):
            for index in range(self.depth-1):
                block += text[i+index]
            cblock.append(len(block))
            block = ""
        for sentence in text:
            indexDistribution.append(len(sentence))
        max_loc = [x for x in range(len(cblock)) if cblock[x] == max(cblock)]
        for begin in range(len(cblock)):
            if cblock[begin] > self.threshold:
                starts[begin] = cblock[begin]
        starts_by_value = sorted(starts.items(),key = lambda e:e[1], reverse = True)
        starts_by_index = sorted(starts.items(),key = lambda e:e[0], reverse = False)
        for ii in starts_by_index:
            index = ii[0]
            for idx in range(self.depth):
                is_start = True
                if cblock[index+idx+1] == 0:
                    is_start = False
            if is_start:
                start = index
                start_bool = True
                print("start:")
                print(start)
                break

        if start_bool:
            for j in range(start, len(cblock)):
                if cblock[j] == 0 and cblock[j+1] == 0:
                    end = j
                    end_bool = True
                    print("end:")
                    print(end)
                    break
        result = ""
        for line in range(start, end):
            result += text[line] + "\n"
        return  result





