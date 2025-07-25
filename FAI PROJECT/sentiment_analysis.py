from textblob import TextBlob
import nltk
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
import ctypes


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

class SentimentAnalyzerApp:
    def __init__(self, root):
        self.root = root
        
        
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
        
        self.root.title("Sentiment Analysis Tool")
        self.root.geometry("800x600")
        self.root.state('zoomed')  
        self.root.tk.call('tk', 'scaling', 1.4)  
        
        self.create_widgets()
        
    def create_widgets(self):

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(
            header_frame, 
            text="Sentiment Analysis Tool", 
            font=("Helvetica", 16, "bold")
        ).pack()
        
        ttk.Label(
            header_frame, 
            text="Enter text to analyze its sentiment", 
            font=("Helvetica", 10)
        ).pack(pady=5)
        
        
        input_frame = ttk.LabelFrame(main_frame, text="Input Text", padding="10")
        input_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.input_text = ScrolledText(
            input_frame, 
            width=80, 
            height=15, 
            font=("Helvetica", 10),
            wrap=tk.WORD
        )
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            button_frame, 
            text="Analyze Sentiment", 
            command=self.analyze_sentiment
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Clear", 
            command=self.clear_text
        ).pack(side=tk.LEFT, padx=5)
        
        
        results_frame = ttk.LabelFrame(main_frame, text="Analysis Results", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        
        results_canvas = tk.Canvas(results_frame)
        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=results_canvas.yview)
        self.scrollable_frame = ttk.Frame(results_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: results_canvas.configure(
                scrollregion=results_canvas.bbox("all")
            )
        )
        
        results_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        results_canvas.configure(yscrollcommand=scrollbar.set)
        
        results_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        ttk.Label(
            self.scrollable_frame, 
            text="Sentiment:", 
            font=("Helvetica", 10, "bold")
        ).grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.sentiment_label = ttk.Label(
            self.scrollable_frame, 
            text="", 
            font=("Helvetica", 12)
        )
        self.sentiment_label.grid(row=0, column=1, sticky=tk.W, pady=(0, 5))
        
       
        ttk.Label(
            self.scrollable_frame, 
            text="Polarity Score:", 
            font=("Helvetica", 10, "bold")
        ).grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.polarity_label = ttk.Label(
            self.scrollable_frame, 
            text="", 
            font=("Helvetica", 12)
        )
        self.polarity_label.grid(row=1, column=1, sticky=tk.W, pady=5)
        
       
        ttk.Label(
            self.scrollable_frame, 
            text="Subjectivity Score:", 
            font=("Helvetica", 10, "bold")
        ).grid(row=2, column=0, sticky=tk.W, pady=5)
        
        self.subjectivity_label = ttk.Label(
            self.scrollable_frame, 
            text="", 
            font=("Helvetica", 12)
        )
        self.subjectivity_label.grid(row=2, column=1, sticky=tk.W, pady=5)
        
       
        self.canvas = tk.Canvas(
            self.scrollable_frame, 
            width=200, 
            height=30, 
            bg='white',
            highlightthickness=1,
            highlightbackground="black"
        )
        self.canvas.grid(row=3, column=0, columnspan=2, pady=10)
        
        
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        
    def analyze_sentiment(self):
        text = self.input_text.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to analyze!")
            return
            
        try:
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity
            
            if polarity > 0.1:
                sentiment = "Positive"
                color = "green"
            elif polarity < -0.1:
                sentiment = "Negative"
                color = "red"
            else:
                sentiment = "Neutral"
                color = "yellow"
            
            
            self.sentiment_label.config(text=sentiment)
            self.polarity_label.config(text=f"{polarity:.4f}")
            self.subjectivity_label.config(text=f"{subjectivity:.4f}")
            
           
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 200, 30, fill=color)
            self.canvas.create_text(
                100, 15, 
                text=sentiment, 
                font=("Helvetica", 10, "bold")
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.sentiment_label.config(text="")
        self.polarity_label.config(text="")
        self.subjectivity_label.config(text="")
        self.canvas.delete("all")
        self.canvas.config(bg='white')

if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalyzerApp(root)
    root.mainloop()