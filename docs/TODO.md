# TO-DO LIST

- Nivel 0x01
  - Melhorar o modelo de IA.
  - Ver como funciona o deploy.
- Nivel 0x02
  - [ ] https://discuss.streamlit.io/t/adding-in-streamlit-chat-input-the-possibility-to-add-an-image/55156/3
    - `import numpy as np; from PIL import Image`
- Nivel 0x03
  - [ ] implementar o venv
  - [ ] verificar se a chave da api carregou

# Notes

- Para usar o `system instruction` precisa do gemini 1.5

```
# old pages/about.py
import streamlit as st

st.write('# Test!')
st.link_button("About the Project", "https://github.com/dantsec")

linkedin, github = st.columns(2)
with linkedin:
    st.link_button('Linkedin', 'https://www.linkedin.com/in/naomilago/')
with github:
    st.link_button('Github', 'https://github.com/naomilago/diver')

# st.page_link("./pages/about.py", label="About Me", icon="👤", use_container_width=True)
```

# Texts to Documentation

```
PT-BR
Dispensa Magica: Descubra o que cozinhar com o que você tem

Desbloqueie a magia da sua dispensa com esta ferramenta! Deixe-nos revelar as possibilidades escondidas nos seus ingredientes, transformando-os em deliciosas refeições.
```

Este chatbot culinário utiliza técnicas de IA (few-shot learning + chain-of-thought) para ajudar usuários a encontrar receitas com base nos ingredientes que possuem em casa. Ele identifica os ingredientes, busca receitas compatíveis, considera restrições e preferências, e apresenta sugestões de forma organizada. O objetivo é mostrar ao usuário como a gastronomia é uma área adaptável e abrangente.

---

```
## License 📋

- [MIT License](./LICENSE)
````

<div align="center">

  <a href="#-authors">Authors</a>&nbsp;•&nbsp;
  <a href="#-stack">Tech Stack</a>&nbsp;•&nbsp;
  <a href="#-installation">Installation</a>&nbsp;•&nbsp;
  <a href="#-livedemo">Livedemo</a>&nbsp;•&nbsp;
  <a href="#-screenshot">Screenshots</a>&nbsp;•&nbsp;
  <a href="#-contributing">Contributing</a>

</div>