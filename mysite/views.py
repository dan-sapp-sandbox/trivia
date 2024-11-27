from django.shortcuts import render
import os

def view_notebook(request, notebook_name):
    # Path to the HTML-converted notebooks
    notebook_path = os.path.join('notebooks', f'{notebook_name}.html')

    if os.path.exists(notebook_path):
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_html = f.read()
        return render(request, 'notebook.html', {'notebook_html': notebook_html})
    else:
        return render(request, '404.html', {'message': 'Notebook not found'})

def serve_notebook(request, notebook_name):
    # Construct the path to the notebook HTML
    template_path = f'notebooks/{notebook_name}.html'

    # Check if the file exists
    if os.path.exists(os.path.join('myapp/templates/', template_path)):
        return render(request, template_path)
    else:
        # Handle the case where the notebook doesn't exist
        return render(request, '404.html', {'message': 'Notebook not found'})
      
def home(request):
  return render(request, 'home.html')