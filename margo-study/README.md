# Studii în Anglia — Margarita Dmitriev

Static, trilingual landing page (Romanian = main, Russian, English) rebuilt from
`margo-study.tilda.ws/studii_in_anglia` with the same content and a new design.

```
index.html        Romanian (main)   → /
ru/index.html     Russian           → /ru/
en/index.html     English           → /en/
assets/           CSS, JS, images, favicon
scripts/build.py  Generates the three pages from one template + translations
vercel.json       Vercel config (static, no build step)
```

## Edit content
All texts (all three languages), contacts and reviews live in `scripts/build.py`.
After editing run:

```bash
python3 scripts/build.py
```

## Contact form
There is no backend: the form opens WhatsApp (+44 7834 241022) with the
visitor's name / phone / e-mail pre-filled.

## Deploy
Vercel project root directory = `margo-study`, framework preset "Other", no build command.
