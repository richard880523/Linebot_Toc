from transitions.extensions import GraphMachine

from utils import send_text_message, send_sticker_message, send_carousel_message, send_video_message, send_button_message, send_carousel_message2
from reptile import link, trending_video

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_init(self, event):
        text = event.message.text
        return text.lower() == "wake"

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == "main"

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "music"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "study"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "funk"

    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "guitar"    

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "video"        
    
    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "news"    

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "movie" 

    def on_enter_user(self, event):
        print("I'm entering user")
        reply_token = event.reply_token
        # send_text_message(reply_token, "hi")
        send_button_message(reply_token)
    def on_exit_user(self, event):
       print("Leaving user")

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        # send_text_message(reply_token, "Trigger state1")
        # send_sticker_message(reply_token)
        send_carousel_message(reply_token)        
        # self.go_back()
    def on_exit_state1(self, event):
       # print(event.message.text)
       print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, link("https://www.youtube.com/results?search_query=reading+music"))
        self.go_back()
    def on_exit_state2(self):
        # print(event.message.text)
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_text_message(reply_token, link("https://www.youtube.com/results?search_query=funk+hip+hop"))
        self.go_back()
    def on_exit_state3(self):
        print("Leaving state3")    

    def on_enter_state4(self, event):
        print("I'm entering state4")
        reply_token = event.reply_token
        send_text_message(reply_token, link("https://www.youtube.com/results?search_query=guitar+beat+music"))
        self.go_back()
    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")
        reply_token = event.reply_token
        send_carousel_message2(reply_token)
    def on_exit_state5(self, event):
        print("Leaving state5")      

    def on_enter_state6(self, event):
        print("I'm entering state6")
        reply_token = event.reply_token
        send_text_message(reply_token, trending_video("https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRa1hidUhVU0RRZVRfdXUta0lvRWVsWg%3D%3D"))
        self.go_back()
    def on_exit_state6(self):
        print("Leaving state6")
    
    def on_enter_state7(self, event):
        print("I'm entering state7")
        reply_token = event.reply_token
        send_text_message(reply_token, trending_video("https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wMnZ4bhIiUEx6akZiYUZ6c21NUjhlWGFfMXU4ZzVTQVJpRnBIYWc1OA%3D%3D"))
        self.go_back()
    def on_exit_state7(self):
        print("Leaving state7")       