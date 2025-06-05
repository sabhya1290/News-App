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
        self.setGeometry(300,200,500,500) 
        self.stack = QStackedLayout()
        self.base()
        self.setLayout(self.stack)
    	
    def base(self):
        self.layout1 = QWidget()

        self.header= QLabel("News Buddy",self)
        self.news_label=QLabel("Want to see Top Headlines or Everything:",self)
        headline=QPushButton("Top Headlines",self)
        everything=QPushButton("Everything",self)
        
        l1=QVBoxLayout()
        l1.addWidget(self.header)
        l1.addWidget(self.news_label)

        h1=QHBoxLayout()
        h1.addWidget(headline)
        h1.addWidget(everything)
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
        headline.clicked.connect(self.Headlines)
        everything.clicked.connect(self.Everything)

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

        self.header= QLabel("News Buddy",self)
        self.news_label=QLabel("Enter Category:",self)
        self.topic_input = QLineEdit(self)
        self.button=QPushButton("Search Headlines",self)
        self.news_title=QLabel(self)
        self.news_description=QLabel(self)
        self.news_url= QLabel(self)
        previous_page=QPushButton("Go Back To Previous Page",self)
        self.image_label=QLabel(self)
        self.image_label.setFixedSize(500, 500) 
        self.image_label.setAlignment(Qt.AlignCenter)

        
        l2=QVBoxLayout()  
        l2.addWidget(self.header)
        hbox=QHBoxLayout()
        hbox.addWidget(self.news_label)
        hbox.addWidget(self.topic_input)
        hbox.addWidget(self.button)
        l2.addLayout(hbox)
        l2.addWidget(self.news_title)
        h=QHBoxLayout()
        v=QVBoxLayout()
        v.addWidget(self.news_description)
        v.addWidget(self.news_url)
        h.addLayout(v)
        h.addWidget(self.image_label)
        l2.addLayout(h)
        l2.addWidget(previous_page)

        self.layout2.setLayout(l2)
        self.stack.addWidget(self.layout2)

        
        l2.setAlignment(Qt.AlignTop)

        self.header.setObjectName("Title")
        self.news_label.setObjectName("Label")
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
        self.stack.setCurrentIndex(1)
        self.button.clicked.connect(self.search_headlines)
        previous_page.clicked.connect(self.previous_page_func)
        
    def Everything(self):
        
        
        self.layout2 = QWidget()

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

        
        l2=QVBoxLayout()  
        l2.addWidget(self.header)
        hbox=QHBoxLayout()
        hbox.addWidget(self.news_Topic)
        hbox.addWidget(self.topic_input)
        hbox.addWidget(self.button_n)
        l2.addLayout(hbox)
        l2.addWidget(self.news_title)
        h=QHBoxLayout()
        v=QVBoxLayout()
        v.addWidget(self.news_description)
        v.addWidget(self.news_url)
        h.addLayout(v)
        h.addWidget(self.image_label)
        l2.addLayout(h)
        l2.addWidget(previous_page)

        self.layout2.setLayout(l2)
        self.stack.addWidget(self.layout2)

        l2.setAlignment(Qt.AlignTop)

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
                            }
                            QLabel#url{
                            font-size:20px;
                            font-family:Arial;       
                            }
                            """)
        self.stack.setCurrentIndex(1)
        self.button_n.clicked.connect(self.search_everything)
        previous_page.clicked.connect(self.previous_page_func)

    def search_headlines(self):
        try:
            category = self.topic_input.text()
            api_key='8c55dd2d96b1494db4cfac382a8acb8a'
            url=f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            
            self.news_title.setText(data['articles'][1]['title'])
            self.news_title.setWordWrap(True)
            self.news_description.setText(data['articles'][1]['description'])
            self.news_description.setWordWrap(True)
            self.news_url.setText(f"url={data['articles'][1]['url']}")
            self.news_url.setWordWrap(True)
            url_image=data['articles'][1]['urlToImage']
            r=requests.get(url_image)
            image_data = BytesIO(r.content)
            pixmap = QPixmap()
            pixmap.loadFromData(image_data.read())
            self.image_label.setPixmap(pixmap.scaled(
                        self.image_label.width(),
                          self.image_label.height(),
                            Qt.KeepAspectRatio))
            
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
        # except KeyError:
        #     self.display_error("Please first search something")
        
    def search_everything(self):
        try:
            
            topic = self.topic_input.text()
            api_key='8c55dd2d96b1494db4cfac382a8acb8a'
            url=f'https://newsapi.org/v2/everything?q={topic}&from=2025-06-04&sortBy=popularity&apiKey={api_key}'
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            
            self.news_title.setText(data['articles'][1]['title'])
            self.news_title.setWordWrap(True)
            self.news_description.setText(data['articles'][1]['description'])
            self.news_description.setWordWrap(True)
            self.news_url.setText(f"url={data['articles'][1]['url']}")
            self.news_url.setWordWrap(True)
            url_image=data['articles'][1]['urlToImage']
            r=requests.get(url_image)
            image_data = BytesIO(r.content)
            pixmap = QPixmap()
            pixmap.loadFromData(image_data.read())
            # self.image_label.setPixmap(pixmap)
            self.image_label.setPixmap(pixmap.scaled(
                        self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))
            
            
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
        self.news_description.setText(message)
        self.news_url.setText("")
        self.image_label.setPixmap(QPixmap())
        
    def display_news(self):
        pass

    def previous_page_func(self):
        self.layout2.deleteLater()
        self.stack.setCurrentIndex(0)



def main():
    app = QApplication(sys.argv)
    window = News_app()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()