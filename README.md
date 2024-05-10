# Magic Pantry @ Gemini AI chatbot Project 🤖

> Magic Pantry: Discover what to cook with what you have. Unlock the magic of your pantry with this tool! Let us reveal the possibilities hidden in your ingredients, turning them into delicious meals.

- **Magic Pantry** is a funny and useful culinary chatbot that uses AI techniques ([**_zero-shot_** + **_chain of thought_**](https://www.promptingguide.ai/techniques/cot.en#zero-shot-cot-prompting)) to help users find recipes based on the ingredients they have at your pantry. Identifies ingredients, searches for compatible recipes, considers restrictions and preferences and presents suggestions in an organized way. The objective is to show to user how it is possible to make a tasty meal even with few resources.

## Authors 👥

- My name is Cauê and I'm graduating in Systems Development Technician at ETEC. I love technology and always seek to learn new knowledge. I am currently interning as a fullstack developer and learning about AI in Alura's immersion was very useful, as it is a growing company.
  - [**@dantsec**](https://www.github.com/dantsec)

## Tech Stack 🧑‍💻

- This project was developed with the following technologies:
  - [**Python**](https://www.python.org/) (Main Language)
    - [**Streamlit**](https://streamlit.io/) (Web Server)

## Installation / Run Locally ⚙️

- **Important**: First of all, you must have [**Python 3 installed**](https://www.python.org/).

- Clone and enter in the project:
```bash
git clone https://github.com/MagicPantry.git && cd MagicPantry/
```

- Run `setup.py`
```bash
python setup.py
```

- Start the server
```bash
python -m streamlit run app.py
```

## Live Demo 🔎

- You can access a live demo clicking [**here**](future-livedemo)!

## Screenshot 📷

> ChatBot homepage.

![homepage](./docs/screenshots/homepage.png)

> Basic use.

![basics](./docs/screenshots/basics.png)

> Leaving the context of AI utility.

![offtopic](./docs/screenshots/offtopic.png)

## Contributing 🛠️

```bash
# Create a fork from MagicPantry repository and clone it.
git clone https://github.com/YOUR_USERNAME/MagicPantry.git
# Enter into the folder.
cd MagicPantry/
# Create a new branch with the name feat-[WHAT_YOUR_FEAT_DO].
git checkout -b feat-[WHAT_YOUR_FEAT_DO]
# Make your changes and commit them.
git add . && git commit -m "YOUR_COMMIT_MESSAGE"
# Push and open a pull request.
git push origin main
```
