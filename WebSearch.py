import tkinter as tk
import webbrowser
import requests
from bs4 import BeautifulSoup


def search(event=None):
    # Get the search term from the entry box
    search_term = search_box.get()
    # Create the search URL
    search_url = "https://www.google.com/search?q=" + search_term
    # Open the search results in the user's default browser
    webbrowser.open(search_url)
    
    try:
        # Get the search results
        res = requests.get(search_url)
        res.raise_for_status() # Raises HTTPError for bad responses (4xx and 5xx)
        
        
    except Exception as e:
        print(f"Error fetching search results: {e}")
        return
    
    
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
    
    # Create a new window to display the search results
    results_window = tk.Toplevel(window)
    results_window.title("Search Results")
    results_window.geometry("600x400")
    
    # Create a frame to hold the search results
    results_frame = tk.Frame(results_window)
    results_frame.pack(fill=tk.BOTH, expand=True)
    
    # Display the search results in the frame
    for i, result in enumerate(results):
        result_label = tk.Label(results_frame, text=result.text)
        result_label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
        

def clear_search():
    #Clear the search box
    search_box.delete(0, tk.END)

# Create the GUI window
window = tk.Tk()
window.title("Web Search")
window.geometry("600x300")
window.config(bg="#1f2833")

# Create the search box label and entry widget
search_label = tk.Label(window, text="Enter your search term:", font=("Arial", 18), bg="#1f2833", fg="#c5c6c7")
search_label.pack(pady=10)
search_box = tk.Entry(window, width=30, font=("Arial", 16), bg="#c5c6c7", fg="#1f2833")
search_box.pack(pady=10)

# Create the search button and bind Enter key to search function
search_button = tk.Button(window, text="Search", font=("Arial", 16), bg="#c5c6c7", fg="#1f2833", command=search)
search_button.pack(pady=10)
window.bind("<Return>", search)

# Create the clear button and bind Escape key to the clear_search function
clear_button = tk.Button(window, text="Clear", command=clear_search)
clear_button.pack(pady=10)
window.bind("<Escape>", lambda event: clear_search())

# Start the GUI event loop
window.mainloop()
