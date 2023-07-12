from flask import url_for

devs = [
    {
        "avatar": url_for("static", filename="images/devs/aman.jpg"),
        "name": "Aman",
        "role": "Project ML Lead",
        "linkedin": "",
        "github": ""
    }, {
        "avatar": url_for("static", filename="images/devs/naved.jpg"),
        "name": "Naved",
        "role": "Project Lead",
        "linkedin": "",
        "github": ""
    }, {
        "avatar": url_for("static", filename="images/devs/ujjwal.png"),
        "name": "Ujjwal Garg",
        "role": "Website designer",
        "linkedin": "https://www.linkedin.com/in/ujjwalgarg100204/",
        "github": "https://www.github.com/ujjwalgarg100204/"
    },
]
