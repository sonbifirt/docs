#!/usr/bin/env python3
"""Generates the static pages (ro = main, ru, en) from one template.

Usage:  python3 scripts/build.py   (run from the margo-study folder or anywhere)
Output: index.html, ru/index.html, en/index.html
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
CUR = ' aria-current="true"'

SITE = "https://studii-in-anglia.vercel.app"
PHONE_DISPLAY = "078 3424 1022"
PHONE_TEL = "+447834241022"
WHATSAPP = "447834241022"
EMAIL = "margo.studentsuk@gmail.com"
FACEBOOK = "https://www.facebook.com/studiiinanglia"
FACEBOOK_REVIEWS = "https://www.facebook.com/studiiinanglia/reviews/?ref=page_internal"
INSTAGRAM = "https://www.instagram.com/margaritadmitriev/"
INSTAGRAM_2 = "https://www.instagram.com/margo_studiiuk/"

LANGS = {
    "ro": {"path": "", "label": "RO", "locale": "ro_RO"},
    "ru": {"path": "ru/", "label": "RU", "locale": "ru_RU"},
    "en": {"path": "en/", "label": "EN", "locale": "en_GB"},
}

UNIVERSITIES = [
    ("arden", "Arden University"),
    ("anglia-ruskin", "Anglia Ruskin University"),
    ("middlesex", "Middlesex University"),
    ("dg-college", "DG College"),
    ("lsc-london", "LSC London"),
    ("london-met", "London Metropolitan University"),
    ("bedfordshire", "University of Bedfordshire"),
    ("lcca", "London College of Contemporary Arts"),
    ("sunderland", "University of Sunderland"),
    ("greenwich", "University of Greenwich"),
    ("bcu", "Birmingham City University"),
    ("uwtsd", "University of Wales Trinity Saint David"),
]

# Reviews are shown verbatim, in the language each student wrote them.
REVIEWS = [
    ("irina", "Irina Kurmei", "https://www.facebook.com/irina.kurmei.1",
     "I recommend with great confidence, everything is well organized, every step is discussed and analyzed, very responsible and communicable person! Professionalism and dedication! Very satisfied with the results!"),
    ("silvia", "Chicus Silvia", "https://www.facebook.com/chicus.silvia",
     "Sunt foarte multumita de ajutorul acordat! Margarita este foarte receptiva, ma ajutat de la inceput pina la sfirsit! Am primit multe recomandari, sfaturi utile si ajutor in toate procedurile intilnite pina la finele inscrierii la universitate! Va multumesc pentru tot!!! Recomand Margarita cu mare incredere!"),
    ("cristina", "Isacov Cristina", "https://www.facebook.com/IsacovCristina",
     "Recomand cu cea mai mare încredere, am primit răspuns la toate întrebările, Doamna Margarita este receptivă, o adevarata profesionistă. Îți mulțumesc pentru informație."),
    ("margarita", "Margarita Belecciu", "https://www.facebook.com/Margarita.Belecciu1993",
     "It offers quality services and receptivity at every stage. Continuous competence and transparency. Thoroughness in explaining and guiding. Thank you!!!"),
    ("valeria", "Valeria Martin", "https://www.facebook.com/valeria.martin.75873",
     "Vreau sa aduc multumiri doamnei Margo pentru toata informatia acordata ce tin de studiile in UK mia explicat foarte bine totul receptiva ai cu o voua buna mult prietenoasa care mia dat multe sfaturi va sugerez cuare drag nu o sa regretati"),
]

T = {
    "ro": {
        "title": "Studii finanțate în Anglia — Aplică acum | Margarita Dmitriev",
        "description": "Aplică la studii în Anglia cu suport gratuit: alegerea universității, documente, interviu, Student Finance. Primești £13.000 pe an pentru cheltuieli personale.",
        "brand": "Studii în Anglia", "brand_sub": "by Margarita Dmitriev",
        "nav": ["De ce să aplici", "Implicarea mea", "Universități", "Recenzii", "Contacte"],
        "cta": "Aplică acum", "call": "Sună acum",
        "badge_tag": "UK", "badge": "Offer support gratuit",
        "h1": "Aplică la studii în <em>Anglia</em>",
        "lead": "Te ajut cu tot procesul <strong>GRATUIT!</strong>",
        "stats": [("£13<span>k</span>", "pentru cheltuieli personale în fiecare an"),
                  ("100<span>+</span>", "cursuri"),
                  ("99<span>%</span>", "Garantez o reușită de 99%")],
        "why_eyebrow": "Beneficii",
        "why_title": "De ce să aplici <em>la studii?</em>",
        "why_sub": "",
        "quote": "„Primești sprijin financiar pentru educație plus £13.000 de lire sterline pentru cheltuieli personale în fiecare an, cu condiția să te califici pentru Student Finance England.”",
        "quote_unit": "/ an",
        "benefits": [
            "Șansa de a avea un JOB plătit și prestigios",
            "Dacă aveți copil, statul vă va oferi + un grant de £2.000. Verificăm eligibilitatea împreună",
            "Posibilitate de aplicare la internship, programe de practică la companii internaționale și programe de voluntariat",
            "Reducere 30% la Oyster Card și Council Tax",
            "Reducere de student la Apple, Amazon, Gym, Asos și alți zeci de parteneri",
            "Diplomă recunoscută mondial",
            "JOB center în cadrul Universității - Te ajut să te angajezi după finalizarea studiilor",
        ],
        "inv_eyebrow": "Cum te ajut",
        "inv_title": "În ce constă <em>implicarea mea?</em>",
        "steps": [
            "Te voi ajuta să alegi Universitate și Cursul potrivit pentru tine",
            "Verificăm documentele pentru aplicare",
            "Te ajut cu pregătirea pentru Interviu și Testul de admitere - <strong>Garantez o reușită de 99%</strong>",
            "Suport în aplicarea la universitate",
            "Consultanță și ghidare în procesul de aplicare la Student Finance",
            "Ajutor pe tot parcursul studiilor",
        ],
        "role": "Studii în Anglia", "online": "Online",
        "uni_eyebrow": "Parteneri",
        "uni_title": "Colaborăm cu zeci de Universități și Colegii <em>cu peste 100 de cursuri</em>",
        "sched_label": "Poți alege program de doar:",
        "sched": ["2 zile pe săptămână", "Flexibil de seară", "ONLINE"],
        "rev_eyebrow": "Recenzii",
        "rev_title": "Ce spun <em>studenții?</em>",
        "rev_all": "Toate recenziile", "rev_src": "Recenzie Facebook",
        "prev": "Înapoi", "next": "Înainte",
        "form_eyebrow": "Completează formularul",
        "form_title": "Beneficiază de consultație <em>GRATUITĂ și PROFESIONISTĂ</em>",
        "form_text": "",
        "form_h": "Studii în Anglia",
        "f_name": "Nume/Prenume", "f_phone": "Telefon", "f_email": "E-mail",
        "f_send": "Trimite", "f_note": "*protejăm datele cu caracter personal",
        "f_ok": "Mulțumim! Mesajul tău a fost pregătit în WhatsApp — apasă „Trimite” acolo.",
        "f_msg": "Bună ziua! Doresc o consultație gratuită pentru studii în Anglia.",
        "contacts": "Contacte", "social": "Social Media",
        "footer_text": "",
        "rights": "Toate drepturile rezervate.",
        "wa_label": "Scrie-ne pe WhatsApp",
        "menu": "Meniu",
    },
    "ru": {
        "title": "Финансируемое обучение в Англии — Подай заявку | Маргарита Дмитриев",
        "description": "Поступление на учёбу в Англии с бесплатным сопровождением: выбор университета, документы, интервью, Student Finance. £13 000 в год на личные расходы.",
        "brand": "Учёба в Англии", "brand_sub": "by Margarita Dmitriev",
        "nav": ["Почему учиться", "Моя помощь", "Университеты", "Отзывы", "Контакты"],
        "cta": "Подать заявку", "call": "Позвонить",
        "badge_tag": "UK", "badge": "Бесплатное сопровождение до оффера",
        "h1": "Поступи на учёбу в <em>Англии</em>",
        "lead": "Помогу со всем процессом <strong>БЕСПЛАТНО!</strong>",
        "stats": [("£13<span>k</span>", "на личные расходы каждый год"),
                  ("100<span>+</span>", "курсов"),
                  ("99<span>%</span>", "Гарантирую успех на 99%")],
        "why_eyebrow": "Преимущества",
        "why_title": "Почему стоит <em>поступать?</em>",
        "why_sub": "",
        "quote": "«Вы получаете финансирование обучения плюс £13 000 фунтов стерлингов на личные расходы каждый год при условии, что вы соответствуете требованиям Student Finance England.»",
        "quote_unit": "/ год",
        "benefits": [
            "Шанс получить оплачиваемую и престижную РАБОТУ",
            "Если у вас есть ребёнок, государство предоставит дополнительный грант £2 000. Проверим ваше право на него вместе",
            "Возможность участвовать в стажировках, программах практики в международных компаниях и волонтёрских программах",
            "Скидка 30% на Oyster Card и Council Tax",
            "Студенческие скидки в Apple, Amazon, спортзалах, Asos и у десятков других партнёров",
            "Диплом, признанный во всём мире",
            "JOB-центр при университете — помогу трудоустроиться после окончания учёбы",
        ],
        "inv_eyebrow": "Как я помогаю",
        "inv_title": "В чём заключается <em>моя помощь?</em>",
        "steps": [
            "Помогу выбрать подходящий именно вам университет и курс",
            "Проверим документы для подачи заявки",
            "Помогу подготовиться к интервью и вступительному тесту — <strong>гарантирую успех на 99%</strong>",
            "Поддержка при подаче заявки в университет",
            "Консультация и сопровождение при подаче заявки в Student Finance",
            "Помощь на протяжении всего обучения",
        ],
        "role": "Учёба в Англии", "online": "Online",
        "uni_eyebrow": "Партнёры",
        "uni_title": "Сотрудничаем с десятками университетов и колледжей <em>более 100 курсов</em>",
        "sched_label": "Можно выбрать программу всего:",
        "sched": ["2 дня в неделю", "Гибкий вечерний график", "ОНЛАЙН"],
        "rev_eyebrow": "Отзывы",
        "rev_title": "Что говорят <em>студенты?</em>",
        "rev_all": "Все отзывы", "rev_src": "Отзыв на Facebook",
        "prev": "Назад", "next": "Вперёд",
        "form_eyebrow": "Заполните форму",
        "form_title": "Получите <em>БЕСПЛАТНУЮ и ПРОФЕССИОНАЛЬНУЮ</em> консультацию",
        "form_text": "",
        "form_h": "Учёба в Англии",
        "f_name": "Имя/Фамилия", "f_phone": "Телефон", "f_email": "E-mail",
        "f_send": "Отправить", "f_note": "*мы защищаем ваши персональные данные",
        "f_ok": "Спасибо! Сообщение подготовлено в WhatsApp — нажмите там «Отправить».",
        "f_msg": "Здравствуйте! Хочу получить бесплатную консультацию по учёбе в Англии.",
        "contacts": "Контакты", "social": "Соцсети",
        "footer_text": "",
        "rights": "Все права защищены.",
        "wa_label": "Написать в WhatsApp",
        "menu": "Меню",
    },
    "en": {
        "title": "Funded Study in England — Apply Now | Margarita Dmitriev",
        "description": "Apply to study in England with free support: choosing a university, documents, interview, Student Finance. Get £13,000 a year for living costs.",
        "brand": "Study in England", "brand_sub": "by Margarita Dmitriev",
        "nav": ["Why apply", "How I help", "Universities", "Reviews", "Contact"],
        "cta": "Apply now", "call": "Call now",
        "badge_tag": "UK", "badge": "Free offer support",
        "h1": "Apply to study in <em>England</em>",
        "lead": "I'll help you through the whole process <strong>for FREE!</strong>",
        "stats": [("£13<span>k</span>", "for personal expenses every year"),
                  ("100<span>+</span>", "courses"),
                  ("99<span>%</span>", "99% success guaranteed")],
        "why_eyebrow": "Benefits",
        "why_title": "Why apply <em>to study?</em>",
        "why_sub": "",
        "quote": "“You receive financial support for your tuition plus £13,000 for personal expenses every year, provided you qualify for Student Finance England.”",
        "quote_unit": "/ year",
        "benefits": [
            "The chance to get a paid and prestigious JOB",
            "If you have a child, the state will give you an extra £2,000 grant. We'll check your eligibility together",
            "Opportunities to apply for internships, work placements at international companies and volunteering programmes",
            "30% discount on the Oyster Card and Council Tax",
            "Student discounts at Apple, Amazon, gyms, Asos and dozens of other partners",
            "A globally recognised degree",
            "University JOB centre — I'll help you get hired after you graduate",
        ],
        "inv_eyebrow": "How I help",
        "inv_title": "What does <em>my support include?</em>",
        "steps": [
            "I'll help you choose the right university and course for you",
            "We check your application documents",
            "I help you prepare for the interview and admission test — <strong>99% success guaranteed</strong>",
            "Support with your university application",
            "Advice and guidance through the Student Finance application",
            "Help throughout your studies",
        ],
        "role": "Study in England", "online": "Online",
        "uni_eyebrow": "Partners",
        "uni_title": "We work with dozens of universities and colleges <em>offering 100+ courses</em>",
        "sched_label": "You can choose a programme of just:",
        "sched": ["2 days a week", "Flexible evenings", "ONLINE"],
        "rev_eyebrow": "Reviews",
        "rev_title": "What do <em>students say?</em>",
        "rev_all": "All reviews", "rev_src": "Facebook review",
        "prev": "Previous", "next": "Next",
        "form_eyebrow": "Fill in the form",
        "form_title": "Get a <em>FREE and PROFESSIONAL</em> consultation",
        "form_text": "",
        "form_h": "Study in England",
        "f_name": "Full name", "f_phone": "Phone", "f_email": "E-mail",
        "f_send": "Send", "f_note": "*we protect your personal data",
        "f_ok": "Thank you! Your message is ready in WhatsApp — just tap “Send” there.",
        "f_msg": "Hello! I'd like a free consultation about studying in England.",
        "contacts": "Contact", "social": "Social media",
        "footer_text": "",
        "rights": "All rights reserved.",
        "wa_label": "Message us on WhatsApp",
        "menu": "Menu",
    },
}

ICONS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "left": '<path d="M15 6l-6 6 6 6"/>',
    "right": '<path d="M9 6l6 6-6 6"/>',
    "wallet": '<path d="M3 7a2 2 0 0 1 2-2h12v4"/><path d="M3 7v10a2 2 0 0 0 2 2h14a1 1 0 0 0 1-1v-8a1 1 0 0 0-1-1H5a2 2 0 0 1-2-2z"/><circle cx="16" cy="14" r="1.2"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "card": '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6.5 15h4"/>',
    "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.3"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14 7 22l5-3 5 3-1.5-8"/>',
    "building": '<path d="M3 21h18M5 21V8l7-5 7 5v13M9 21v-5h6v5M9 10h.01M15 10h.01"/>',
    "calendar": '<rect x="3" y="4.5" width="18" height="16" rx="2.5"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4"/>',
    "moon": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
    "laptop": '<rect x="4" y="4" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="m3 6 9 7 9-7"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
}
FILLED = {
    "star": '<path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4l-5.9 3.1 1.2-6.5L2.5 9.4l6.6-.9z"/>',
    "facebook": '<path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7.1V12h3V9.4c0-3 1.8-4.7 4.6-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/>',
    "instagram": '<path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 4 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zM12 0C8.7 0 8.3 0 7.1.1 2.7.3.3 2.7.1 7.1 0 8.3 0 8.7 0 12s0 3.7.1 4.9c.2 4.4 2.6 6.8 7 7 1.2.1 1.6.1 4.9.1s3.7 0 4.9-.1c4.4-.2 6.8-2.6 7-7 .1-1.2.1-1.6.1-4.9s0-3.7-.1-4.9c-.2-4.4-2.6-6.8-7-7C15.7 0 15.3 0 12 0zm0 5.8a6.2 6.2 0 1 0 0 12.4 6.2 6.2 0 0 0 0-12.4zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.4-11.8a1.4 1.4 0 1 0 0 2.9 1.4 1.4 0 0 0 0-2.9z"/>',
    "whatsapp": '<path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-.9 1.2-.3.2-.6.1a8.2 8.2 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 0 0-.8.4 3.4 3.4 0 0 0-1 2.5 5.9 5.9 0 0 0 1.2 3.1 13.5 13.5 0 0 0 5.2 4.6c1.9.8 2.7.9 3.6.7a3.1 3.1 0 0 0 2-1.4 2.5 2.5 0 0 0 .2-1.4c-.1-.1-.3-.2-.6-.3zM12 21.8a9.8 9.8 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zM20.5 3.5A11.8 11.8 0 0 0 1.9 17.7L.2 24l6.4-1.7A11.8 11.8 0 0 0 24 12a11.7 11.7 0 0 0-3.5-8.5z"/>',
}


def icon(name):
    if name in FILLED:
        return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{FILLED[name]}</svg>'
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def render(lang):
    t = T[lang]
    p = "../" if LANGS[lang]["path"] else ""  # relative prefix to site root
    a = f"{p}assets/"
    ids = ["beneficii", "implicare", "universitati", "recenzii", "contact"]

    lang_links = "".join(
        f'<a href="{p}{v["path"] or "./"}" hreflang="{k}" lang="{k}"'
        f'{CUR if k == lang else ""}>{v["label"]}</a>'
        for k, v in LANGS.items()
    )
    alternates = "\n  ".join(
        f'<link rel="alternate" hreflang="{k}" href="{SITE}/{v["path"]}">' for k, v in LANGS.items()
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}/">\n  <link rel="canonical" href="{SITE}/{LANGS[lang]["path"]}">'
    nav = "".join(f'<a href="#{i}">{n}</a>' for i, n in zip(ids, t["nav"]))
    stats = "".join(f'<div class="stat"><b>{b}</b><small>{s}</small></div>' for b, s in t["stats"])

    b = t["benefits"]
    ben_icons = ["briefcase", "heart", "globe", "card", "tag", "award", "building"]
    benefits = "".join(
        f'<article class="benefit reveal{" benefit--wide" if i == 6 else ""}" style="--d:{(i % 4) * .08:.2f}s">'
        f'<div class="benefit__icon">{icon(ic)}</div><p>{escape(txt)}</p></article>'
        for i, (ic, txt) in enumerate(zip(ben_icons, b))
    )
    steps = "".join(f'<li class="step reveal" style="--d:{i * .06:.2f}s"><p>{s}</p></li>'
                    for i, s in enumerate(t["steps"]))

    def logos(items):
        cells = "".join(
            f'<div class="uni"><img src="{a}img/logo-{k}.webp" alt="{escape(n)}" decoding="async"></div>'
            for k, n in items)
        dup = "".join(
            f'<div class="uni" aria-hidden="true"><img src="{a}img/logo-{k}.webp" alt="" decoding="async"></div>'
            for k, n in items)
        return cells + dup

    sched = "".join(
        f'<div class="chip reveal" style="--d:{i * .08:.2f}s"><span class="chip__icon">{icon(ic)}</span>{s}</div>'
        for i, (ic, s) in enumerate(zip(["calendar", "moon", "laptop"], t["sched"])))

    stars = icon("star") * 5
    reviews = "".join(
        f'<article class="review"><span class="review__quote" aria-hidden="true">“</span>'
        f'<div class="stars" aria-label="5/5">{stars}</div>'
        f'<p lang="{"en" if k in ("irina", "margarita") else "ro"}">{escape(txt)}</p>'
        f'<div class="review__who"><img src="{a}img/r-{k}.webp" alt="{escape(n)}" width="54" height="54" decoding="async">'
        f'<div><b><a href="{fb}" target="_blank" rel="noopener">{escape(n)}</a></b>'
        f'<small>{icon("facebook")}{t["rev_src"]}</small></div></div></article>'
        for k, n, fb, txt in REVIEWS)

    return f"""<!DOCTYPE html>
<html lang="{lang}" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{escape(t["title"])}</title>
  <meta name="description" content="{escape(t["description"])}">
  <meta name="theme-color" content="#0b1726">
  <meta name="format-detection" content="telephone=no">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(t["title"])}">
  <meta property="og:description" content="{escape(t["description"])}">
  <meta property="og:image" content="{SITE}/assets/img/og.jpg">
  <meta property="og:locale" content="{LANGS[lang]["locale"]}">
  {alternates}
  <link rel="icon" href="{a}favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,600;1,700&display=swap&subset=cyrillic" rel="stylesheet">
  <link rel="preload" as="image" href="{a}img/hero.webp">
  <link rel="stylesheet" href="{a}style.css">
</head>
<body>

<header class="header">
  <div class="container header__inner">
    <a class="logo" href="{p}{LANGS[lang]["path"] or './'}" aria-label="{t["brand"]}">
      <span class="logo__mark">M</span>
      <span class="logo__text">{t["brand"]}<small>{t["brand_sub"]}</small></span>
    </a>
    <nav class="nav" aria-label="{t["menu"]}">
      <div class="nav__links">{nav}</div>
      <div class="lang">{lang_links}</div>
      <a class="btn" href="#contact">{t["cta"]}</a>
      <button class="burger" type="button" aria-label="{t["menu"]}" aria-expanded="false"><span></span></button>
    </nav>
  </div>
</header>

<main>
  <section class="hero">
    <div class="hero__bg" role="img" aria-label="Margarita Dmitriev"></div>
    <div class="hero__squares" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
    <div class="container">
      <div class="hero__content">
        <span class="badge reveal"><b>{t["badge_tag"]}</b>{t["badge"]}</span>
        <h1 class="reveal" style="--d:.1s">{t["h1"]}</h1>
        <p class="hero__lead reveal" style="--d:.2s">{t["lead"]}</p>
        <div class="hero__actions reveal" style="--d:.3s">
          <a class="btn" href="#contact">{t["cta"]} {icon("arrow")}</a>
          <a class="btn btn--ghost" href="tel:{PHONE_TEL}">{icon("phone")} {t["call"]}</a>
        </div>
        <div class="stats reveal" style="--d:.4s">{stats}</div>
      </div>
    </div>
    <a class="scroll-cue" href="#beneficii" aria-label="{t["nav"][0]}"></a>
  </section>

  <section class="section" id="beneficii">
    <div class="container">
      <div class="section__head">
        <div class="reveal"><span class="eyebrow">{t["why_eyebrow"]}</span><h2 class="h2">{t["why_title"]}</h2></div>
        {f'<p class="reveal" style="--d:.1s">{t["why_sub"]}</p>' if t["why_sub"] else ""}
      </div>
      <div class="benefits">
        <article class="benefit benefit--feature reveal">
          <div class="benefit__icon">{icon("wallet")}</div>
          <div class="big">£13.000<span>{t["quote_unit"]}</span></div>
          <blockquote>{escape(t["quote"])}</blockquote>
        </article>
        {benefits}
      </div>
    </div>
  </section>

  <section class="section involve" id="implicare">
    <div class="container involve__grid">
      <div class="portrait reveal">
        <span class="portrait__sq portrait__sq--a" aria-hidden="true"></span>
        <div class="portrait__img">
          <img src="{a}img/margarita.webp" alt="Margarita Dmitriev" loading="lazy" width="900" height="1350">
          <div class="portrait__card">
            <div><b>Margarita Dmitriev</b><small>{t["role"]}</small></div>
            <span class="dot" title="{t["online"]}"></span>
          </div>
        </div>
        <span class="portrait__sq portrait__sq--b" aria-hidden="true"></span>
      </div>
      <div>
        <div class="reveal"><span class="eyebrow">{t["inv_eyebrow"]}</span><h2 class="h2">{t["inv_title"]}</h2></div>
        <ol class="steps">{steps}</ol>
        <div class="involve__cta reveal">
          <a class="btn" href="#contact">{t["cta"]} {icon("arrow")}</a>
          <a class="btn btn--ghost" href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">{icon("whatsapp")} WhatsApp</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="universitati">
    <div class="container unis__head reveal">
      <span class="eyebrow">{t["uni_eyebrow"]}</span>
      <h2 class="h2">{t["uni_title"]}</h2>
    </div>
    <div class="marquee"><div class="marquee__track">{logos(UNIVERSITIES[:6])}</div></div>
    <div class="marquee marquee--rev"><div class="marquee__track">{logos(UNIVERSITIES[6:])}</div></div>
    <div class="container schedule">
      <div class="schedule__label reveal">{t["sched_label"]}</div>
      {sched}
    </div>
  </section>

  <section class="section reviews" id="recenzii">
    <div class="container">
      <div class="section__head">
        <div class="reveal"><span class="eyebrow">{t["rev_eyebrow"]}</span><h2 class="h2">{t["rev_title"]}</h2></div>
        <div class="reviews__nav reveal">
          <button class="round" type="button" data-slide="-1" aria-label="{t["prev"]}">{icon("left")}</button>
          <button class="round" type="button" data-slide="1" aria-label="{t["next"]}">{icon("right")}</button>
        </div>
      </div>
      <div class="slider reveal">{reviews}</div>
      <div class="reviews__all"><a class="btn btn--dark" href="{FACEBOOK_REVIEWS}" target="_blank" rel="noopener">{t["rev_all"]} {icon("arrow")}</a></div>
    </div>
  </section>

  <section class="cta" id="contact">
    <div class="container">
      <div class="cta__card reveal">
        <div class="cta__info">
          <span class="eyebrow">{t["form_eyebrow"]}</span>
          <h2 class="h2">{t["form_title"]}</h2>
          {f'<p>{t["form_text"]}</p>' if t["form_text"] else ""}
          <div class="cta__contacts">
            <a href="tel:{PHONE_TEL}"><span>{icon("phone")}</span>{PHONE_DISPLAY}</a>
            <a href="mailto:{EMAIL}"><span>{icon("mail")}</span>{EMAIL}</a>
            <a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener"><span>{icon("whatsapp")}</span>WhatsApp</a>
          </div>
        </div>
        <form class="form" novalidate data-wa="{WHATSAPP}" data-msg="{escape(t["f_msg"])}"
              data-l-name="{escape(t["f_name"])}" data-l-phone="{escape(t["f_phone"])}" data-l-email="{escape(t["f_email"])}">
          <h3>{t["form_h"]}</h3>
          <div class="field"><input id="f-name" name="name" type="text" autocomplete="name" placeholder=" " required><label for="f-name">{t["f_name"]}</label></div>
          <div class="field"><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder=" " required><label for="f-phone">{t["f_phone"]}</label></div>
          <div class="field"><input id="f-email" name="email" type="email" autocomplete="email" placeholder=" " required><label for="f-email">{t["f_email"]}</label></div>
          <button class="btn" type="submit">{t["f_send"]} {icon("arrow")}</button>
          <p class="form__note">{icon("shield")}{t["f_note"]}</p>
          <p class="form__ok" role="status">{t["f_ok"]}</p>
        </form>
      </div>
    </div>
  </section>
</main>

<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <a class="logo" href="{p}{LANGS[lang]["path"] or './'}"><span class="logo__mark">M</span><span class="logo__text">{t["brand"]}<small>{t["brand_sub"]}</small></span></a>
        {f'<p>{t["footer_text"]}</p>' if t["footer_text"] else ""}
      </div>
      <div>
        <h4>{t["contacts"]}</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{icon("phone")}{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{icon("mail")}{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t["social"]}</h4>
        <ul>
          <li><a href="{FACEBOOK}" target="_blank" rel="noopener">{icon("facebook")}Facebook</a></li>
          <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">{icon("instagram")}Instagram</a></li>
          <li><a href="{INSTAGRAM_2}" target="_blank" rel="noopener">{icon("instagram")}@margo_studiiuk</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> {t["brand"]} · Margarita Dmitriev. {t["rights"]}</span>
      <span class="lang">{lang_links}</span>
    </div>
  </div>
</footer>

<a class="fab" href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener" aria-label="{t["wa_label"]}">{icon("whatsapp")}</a>

<script src="{a}main.js" defer></script>
</body>
</html>
"""


def main():
    for lang, meta in LANGS.items():
        out = ROOT / meta["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(lang), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
