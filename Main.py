import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QStackedLayout, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from io import BytesIO


class News_app(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("News Buddy")
        self.setGeometry(400,200,700,600) 
        self.stack = QStackedLayout()
        self.base()
        self.setLayout(self.stack)
    	
    def base(self):
        self.layout1 = QWidget()

        self.header= QLabel("News Buddy",self)
        self.news_label=QLabel("Want to see Top Headlines or Everything:",self)
        self.headline=QPushButton("Top Headlines",self)
        self.everything=QPushButton("Everything",self)
        
        l1=QVBoxLayout()
        l1.addWidget(self.header)
        l1.addWidget(self.news_label)

        h1=QHBoxLayout()
        h1.addWidget(self.headline)
        h1.addWidget(self.everything)
        l1.addLayout(h1)
        l1.setAlignment(Qt.AlignTop)
        
        self.header.setObjectName("Title")
        self.news_label.setObjectName("Label")

        self.layout1.setStyleSheet("""
                            QPushButton{
                           font-size: 30px;
                           font-family: Bahnschrift;
                           }
                           QLabel#Title{
                            font-size:40px; 
                            font-family:Algerian;
                            font -weight: bold;
                           }
                           QLabel#Label{
                            font-size: 30px;
                           font-family: Bahnschrift;
                           }
                            """)
    
        self.layout1.setLayout(l1)
        self.stack.addWidget(self.layout1)
        self.headline.clicked.connect(self.Headlines)
        self.everything.clicked.connect(self.Everything)

    def initUI(self):
        pass
        vbox= QVBoxLayout()
        vbox.addWidget(self.header)
        vbox.addWidget(self.news_label)
        hbox=QHBoxLayout()
        hbox.addWidget(self.headline)
        hbox.addWidget(self.everything)
        vbox.addLayout(hbox)
        # vbox.addWidget(self.news_title)
        # vbox.addWidget(self.news_description)
        self.setLayout(vbox)

        self.header.setAlignment(Qt.AlignTop)

        self.header.setObjectName("Title")
        self.news_label.setObjectName("Label")

        self.setStyleSheet("""
                            QPushButton{
                           font-size: 30px;
                           font-family: Bahnschrift;
                           }
                           QLabel#Title{
                            font-size:40px; 
                            font-family:Algerian;
                            font -weight: bold;
                           }
                           QLabel#Label{
                            font-size: 30px;
                           font-family: Bahnschrift;
                           }
                            """)
        

        self.headline.clicked.connect(self.Headlines)

    def Headlines(self):
        self.layout2 = QWidget()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.layout2)

        self.header= QLabel("News Buddy",self)
        self.news_label=QLabel("Enter Category:",self)
        self.topic_input = QLineEdit(self)
        self.button=QPushButton("Search Headlines",self)
        self.news_title=QLabel(self)
        self.news_description=QLabel(self)
        self.news_url= QLabel(self)
        previous_page=QPushButton("Go Back To Previous Page",self)
        self.image_label=QLabel(self)
        self.image_label.setFixedSize(400, 400) 
        self.image_label.setAlignment(Qt.AlignCenter)
        # self.error_label=QLabel(self)
        self.next_article=QPushButton("Next Article",self)
        self.previous_article=QPushButton("Previous Article",self)
        self.page=0

        
        self.l2=QVBoxLayout()  
        self.l2.addWidget(self.header)
        self.hbox=QHBoxLayout()
        self.hbox.addWidget(self.news_label)
        self.hbox.addWidget(self.topic_input)
        self.hbox.addWidget(self.button)
        self.l2.addLayout(self.hbox)
        
        
        self.l2.addLayout(self.hbox)
        self.l2.addWidget(self.news_title)
        # self.l2.addWidget(self.error_label)
        h=QHBoxLayout()
        v=QVBoxLayout()
        v.addWidget(self.news_description)
        v.addWidget(self.news_url)
        h.addLayout(v)
        h.addWidget(self.image_label)
        self.l2.addLayout(h)
        self.h1=QHBoxLayout()
        self.h1.addWidget(previous_page)
        self.l2.addLayout(self.h1)
        self.layout2.setLayout(self.l2)
        self.stack.addWidget(scroll)
        self.button.clicked.connect(self.search_headlines)

        
        self.l2.setAlignment(Qt.AlignTop)

        self.header.setObjectName("Title")
        self.news_label.setObjectName("Label")
        self.news_title.setObjectName("news_title")
        self.news_description.setObjectName("description")
        self.news_url.setObjectName("url")
        # self.error_label.setObjectName("error")


        self.layout2.setStyleSheet("""
                            QPushButton, QLineEdit {
                           font-size: 20px;
                           font-family: Bahnschrift;
                           }
                           QLabel#Title{
                            font-size:40px; 
                            font-family:Algerian;
                            font -weight: bold;
                           }
                           QLabel#Label{
                            font-size: 20px;
                            font-family: Bahnschrift;
                           }
                           QLabel#news_title{
                            font-size:30px;
                            font-family:Arial;
                            font -weight: bold;
                            text-decoration:underline;       
                            }
                            QLabel#description{
                            font-size:20px;
                            font-family:Arial;       
                            }
                            QLabel#url{
                            font-size:20px;
                            font-family:Arial;       
                            }
                            
                            """)
        self.stack.setCurrentIndex(1)
        self.stack.setCurrentWidget(scroll)
        
        
        previous_page.clicked.connect(self.previous_page_func)
        
    def Everything(self):
        
        
        self.layout2 = QWidget()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.layout2)


        self.header= QLabel("News Buddy",self)
        self.news_Topic=QLabel("Enter Topic:",self)
        self.topic_input = QLineEdit(self)
        self.button_n=QPushButton("Search News",self)
        self.news_title=QLabel(self)
        self.news_description=QLabel(self)
        self.news_url= QLabel(self)
        previous_page=QPushButton("Go Back To Previous Page",self)
        self.image_label=QLabel(self)
        self.image_label.setFixedSize(300, 300)  
        self.image_label.setAlignment(Qt.AlignCenter)
        self.next_article=QPushButton("Next Article",self)
        self.previous_article=QPushButton("Previous Article",self)
        self.page=0

        
        self.l2=QVBoxLayout()  
        self.l2.addWidget(self.header)
        hbox=QHBoxLayout()
        hbox.addWidget(self.news_Topic)
        hbox.addWidget(self.topic_input)
        hbox.addWidget(self.button_n)
        self.l2.addLayout(hbox)
        self.l2.addWidget(self.news_title)
        h=QHBoxLayout()
        v=QVBoxLayout()
        v.addWidget(self.news_description)
        v.addWidget(self.news_url)
        h.addLayout(v)
        h.addWidget(self.image_label)
        self.l2.addLayout(h)
        self.h1=QHBoxLayout()
        self.h1.addWidget(previous_page)
        self.l2.addLayout(self.h1)

        self.layout2.setLayout(self.l2)
        self.stack.addWidget(scroll)
        self.button_n.clicked.connect(self.search_everything)

        self.l2.setAlignment(Qt.AlignTop)

        self.header.setObjectName("Title")
        self.news_Topic.setObjectName("Label")
        self.news_title.setObjectName("news_title")
        self.news_description.setObjectName("description")
        self.news_url.setObjectName("url")

        self.layout2.setStyleSheet("""
                            QPushButton, QLineEdit {
                           font-size: 20px;
                           font-family: Bahnschrift;
                           }
                           QLabel#Title{
                            font-size:40px; 
                            font-family:Algerian;
                            font -weight: bold;
                           }
                           QLabel#Label{
                            font-size: 20px;
                            font-family: Bahnschrift;
                           }
                           QLabel#news_title{
                            font-size:30px;
                            font-family:Arial;
                            font -weight: bold;
                            text-decoration:underline;       
                            }
                            QLabel#description{
                            font-size:20px;
                            font-family:Arial;
                            color:black;       
                            }
                            QLabel#url{
                            font-size:20px;
                            font-family:Arial;       
                            }
                            """)
        self.stack.setCurrentIndex(1)
        self.stack.setCurrentWidget(scroll)

        previous_page.clicked.connect(self.previous_page_func)

    def search_headlines(self):
        try:
            category = self.topic_input.text()
            api_key='8c55dd2d96b1494db4cfac382a8acb8a'
            url=f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            totalresult=data['totalResults']
            
            if self.page==0:
                self.h1.addWidget(self.next_article)
                self.h1.addWidget(self.previous_article)
                self.layout2.setLayout(self.h1)
            self.next_article.clicked.connect(self.next_page_func)
            self.previous_article.clicked.connect(self.previous_article_func)

            news=data['articles']

            if self.page>totalresult:
                self.next_article.setEnabled(False)
            else:
                self.next_article.setEnabled(True)

            if self.page<1:
                self.previous_article.setEnabled(False)
            else:
                self.previous_article.setEnabled(True)

            self.news_title.setText(news[self.page]['title'])
            print(self.page)
            self.news_title.setWordWrap(True)
            self.news_description.setText(news[self.page]['description'])
            self.news_description.setWordWrap(True)
            self.news_description.setStyleSheet("font-size:20px;"
                                            "color: black")
            self.news_url.setText(f"url={news[self.page]['url']}")
            self.news_url.setWordWrap(True)
            url_image=news[self.page]['urlToImage']
            r=requests.get(url_image)
            if r.status_code==200:
                image_data = BytesIO(r.content)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data.read())
                self.image_label.setPixmap(pixmap.scaled(
                            self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))
            else:
                pass
            
        except requests.exceptions.HTTPError as http_error: 
            match response.status_code: 
                case 400: 
                    self.display_error("Bad request: \nPlease check your input") 
                case 401: 
                    self.display_error("Unauthorized:\nInvalid API key") 
                case 429: 
                    self.display_error("Too Many Requests: \nYou made too many requests within a window of time and have been rate limited. Back off for a while") 
                case 404: 
                    self.display_error("Not found: \nCity not found") 
                case 500: 
                    self.display_error("Internal Server Error: \nPlease try again later") 
                case _:
                    self.display_error("An error occurred")
        
        except requests.exceptions.ConnectionError: 
            self.display_error("Connection Error: \nCheck your internet connection") 
        except requests.exceptions.Timeout: 
            self.display_error("Timeout Error: \nThe request timed out") 
        except requests.exceptions.TooManyRedirects: 
            self.display_error("Too many Redirects: \nCheck the URL") 
        except requests.exceptions.RequestException as req_error:             
            self.display_error(f"Request Error: \n{req_error}")  
        
        except IndexError:
            self.display_error("No news found for the given topic")
        
    def search_everything(self):
        try:
            
            topic = self.topic_input.text()
            api_key='8c55dd2d96b1494db4cfac382a8acb8a'
            url=f'https://newsapi.org/v2/everything?q={topic}&from=2025-06-04&sortBy=popularity&apiKey={api_key}'
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()

            self.h1.addWidget(self.next_article)
            self.h1.addWidget(self.previous_article)
            self.layout2.setLayout(self.h1)
            self.next_article.clicked.connect(self.next_page_func)
            self.previous_article.clicked.connect(self.previous_article_func)
            
            self.news_title.setText(data['articles'][self.page]['title'])
            self.news_title.setWordWrap(True)
            self.news_description.setText(data['articles'][self.page]['description'])
            self.news_description.setWordWrap(True)
            self.news_description.setStyleSheet("font-size:20px;"
                                            "color: black")
            self.news_url.setText(f"url={data['articles'][self.page]['url']}")
            self.news_url.setWordWrap(True)
            url_image=data['articles'][self.page]['urlToImage']
            r=requests.get(url_image)
            if r.status_code==200:
                image_data = BytesIO(r.content)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data.read())
                self.image_label.setPixmap(pixmap.scaled(
                            self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))
            else:
                pass
            
        except requests.exceptions.HTTPError as http_error: 
            match response.status_code: 
                case 400: 
                    self.display_error("Bad request: \nPlease check your input") 
                case 401: 
                    self.display_error("Unauthorized:\nInvalid API key") 
                case 429: 
                    self.display_error("Too Many Requests: \nYou made too many requests within a window of time and have been rate limited. Back off for a while") 
                case 404: 
                    self.display_error("Not found: \nCity not found") 
                case 500: 
                    self.display_error("Internal Server Error: \nPlease try again later") 
                case _:
                    self.display_error("An error occurred")
        
        except requests.exceptions.ConnectionError: 
            self.display_error("Connection Error: \nCheck your internet connection") 
        except requests.exceptions.Timeout: 
            self.display_error("Timeout Error: \nThe request timed out") 
        except requests.exceptions.TooManyRedirects: 
            self.display_error("Too many Redirects: \nCheck the URL") 
        except requests.exceptions.RequestException as req_error:             
            self.display_error(f"Request Error: \n{req_error}")  
        
        except IndexError:
            self.display_error("No news found for the given topic")
        except KeyError:
            self.display_error("Please first search something")
               
    def display_error(self,message):
        self.news_title.setText("")
        self.news_url.setText("")
        self.news_description.setText(message)
        self.image_label.setPixmap(QPixmap())
        self.news_description.setStyleSheet("font-size:30px;"
                                            "color: red")

        
    def display_news(self,data):
        pass
        for i in range(5):
                self.news_title=QLabel(self)
                self.news_description=QLabel(self)
                self.news_url= QLabel(self)
                # previous_page=QPushButton("Go Back To Previous Page",self)
                self.image_label=QLabel(self)
                self.image_label.setFixedSize(200, 200) 
                self.image_label.setAlignment(Qt.AlignCenter)
                self.news_title.setText(data['articles'][i]['title'])
                self.news_title.setWordWrap(True)
                self.news_description.setText(data['articles'][i]['description'])
                self.news_description.setWordWrap(True)
                self.news_url.setText(f"url={data['articles'][i]['url']}")
                self.news_url.setWordWrap(True)
                url_image=data['articles'][i]['urlToImage']
                
                
                r=requests.get(url_image)
                image_data = BytesIO(r.content)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data.read())
                self.image_label.setPixmap(pixmap.scaled(
                                self.image_label.width(),
                                self.image_label.height(),
                                    Qt.KeepAspectRatio))
                
                        
                
                
                self.l2.addWidget(self.news_title)
                h=QHBoxLayout()
                v=QVBoxLayout()
                v.addWidget(self.news_description)
                v.addWidget(self.news_url)
                h.addLayout(v)
                h.addWidget(self.image_label)
                self.l2.addLayout(h)
                
                self.news_title.setObjectName("news_title")
                self.news_description.setObjectName("description")
                self.news_url.setObjectName("url")

                self.layout2.setStyleSheet("""
                            QPushButton, QLineEdit {
                           font-size: 20px;
                           font-family: Bahnschrift;
                           }
                           QLabel#Title{
                            font-size:40px; 
                            font-family:Algerian;
                            font -weight: bold;
                           }
                           QLabel#Label{
                            font-size: 20px;
                            font-family: Bahnschrift;
                           }
                           QLabel#news_title{
                            font-size:30px;
                            font-family:Arial;
                            font -weight: bold;
                            text-decoration:underline;       
                            }
                            QLabel#description{
                            font-size:20px;
                            font-family:Arial;       
                            }
                            QLabel#url{
                            font-size:20px;
                            font-family:Arial;       
                            }
                            """)
                # self.button.clicked.connect(self.search_headlines)


    def previous_page_func(self):
        current_widget = self.stack.currentWidget()
        self.stack.removeWidget(current_widget)
        self.layout2.deleteLater()
        self.stack.setCurrentIndex(0)

    def next_page_func(self):
        self.page+=1
        if self.headline.clicked:
            self.search_headlines()
        else:
            self.search_everything()

    def previous_article_func(self):
        self.page-=1
        if self.headline.clicked:
            self.search_headlines()
        else:
            self.search_everything()

def main():
    app = QApplication(sys.argv)
    window = News_app()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()