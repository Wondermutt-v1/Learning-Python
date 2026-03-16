#
# Example file for working with HTML data
# LinkedIn Learning Python course
#

#

from html.parser import HTMLParser

paragraphs = 0


class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        print("Encountered comment:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position:", pos[1])
        
    def handle_starttag(self,tag, attrs):
        print("Encountered start tag:", tag)
        pos = self.getpos()
        print("At line:", pos[0], "position:", pos[1])
        
        global paragraphs
        if tag == "p":
            paragraphs += 1
            
        if attrs.__len__() > 0:
            print("Attributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])
            
    def handle_data(self,data):
        print("Encountered the textdata:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position:", pos[1])
    
    
    
    
    
def main():
    # instantiate the parser and feed it some HTML
    parser= MyHTMLParser()
    
    f= open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read() # read the entire file
        parser.feed(contents)
    
    print(paragraphs, "paragraphs found")
        
        
if __name__ == "__main__":
    main()