import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='App to help to organize flask apps')
    
    parser.add_argument('--new', type=str, help='creates simple template for flask project')

    args = parser.parse_args()

    if args.new:
        print(f'Creating project with a name of: {args.new}')
        directory_name = Path(args.new)
        try:
            print(f'Creating directory: {args.new}')
            directory_name.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print(f'{args.new} already exists')
        else:
            static_directory = directory_name / "static"
            print('Creating /static directory')
            static_directory.mkdir(parents=True, exist_ok=True)
            print('Creating styles')
            style_file = static_directory / "style.css"
            style_file.write_text("")

            template_directry = directory_name / "templates" 
            print('Creating /templates directory')
            template_directry.mkdir(parents=True, exist_ok=True)
            print('Creating index page')
            html_file = template_directry / "index.html"
            print('Adding base content to index page')
            html_file.write_text("<!DOCTYPE html>\n<html>\n\t<head>\n\n\t</head>\n\n\t<body>\n\n\t</body>\n</html>")
            
            print('Creating base python file')
            python_file = directory_name / str(args.new+".py")
            print('Filling python file with base code')
            python_file.write_text("from flask import Flask, render_template\n\napp = Flask(__name__)\n\n@app.route('/')\n\ndef index():\n\treturn render_template('index.html')\n\nif __name__ == '__main__':\n\tapp.run(debug=True)")

if __name__ == "__main__":
    main()
