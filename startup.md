# Startup

## First input

Execute the Populate.py file in the root directory to load the documents the first time with

```bash
   python3 Populate.py
```

## Api

The main logic for the processing is in the api. To run it run the following command in the root directory:

```bash
uvicorn src.Code.App:app --reload 
```

The api will be running on `http://localhost:8000`.

## Frontend

The frontend is a simple blazor app. To run it run the following command in the root directory:

```bash
dotnet watch run --project src/Gui
```

The frontend will be running on `http://localhost:5200`. It has a simple text input where you can type the query to search for. 

Autocomplete ghost text may appear suggesting the most common words in the documents, use `Tab` to autocomplete.

The search is case-insensitive and will return the documents that contain the query.

When clicking the document, a card will appear with all the details of the book.
