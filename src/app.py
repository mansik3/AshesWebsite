from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    game = {
        'title': 'Ashes',
        'title_img': 'img/titleImg.png',
        'tagline': 'Gather the Embers. Save the Cosmos.',
        'overview': (
            "In a shattered cosmos once unified by the Divine Aurora Virelia, an ancient Void splintered all life. "
            "You are the prophesied Flameborne, reborn from the ashes of the Fallen Star in Verdant Hollow. "
            "Your quest: gather five scattered embers from realms of ice, magma, astral light, and echoing time. "
            "Along the way, forge alliances and face impossible choices: protect civilization’s fragile hope, "
            "or seize the embers’ power to reshape the universe under your will. Every puzzle solved and enemy vanquished "
            "brings you closer to rekindling Virelia—or plunging existence into eternal shadow."
        ),
        'features': [
            {'title': 'Dynamic Classes', 'desc': 'Choose from Warriors, Mages, Archers, and more — each with unique skill trees.'},
            {'title': 'Environmental Puzzles', 'desc': 'Manipulate time, gravity, fire, and elemental cycles to unlock secrets.'},
            {'title': 'Branching Narrative', 'desc': 'Critical mid-game choices reshape allies, environments, and ending.'},
            {'title': 'Epic Boss Fights', 'desc': 'Confront powerful guardians in each realm — and your own fate.'},
        ],
        'worlds': [
            {'name': 'Verdant Hollow (Forest)', 'desc': 'Overgrown ruins and bioluminescent flora hide the First Ember beneath ancient temples.'},
            {'name': 'Frostbound Sanctuary (Ice)', 'desc': 'Glacial islands under aurora-lit skies, where frost and light converge.'},
            {'name': 'Obsidian Depths (Magma)', 'desc': 'Molten rivers and runic forges test your heat resistance and puzzle acumen.'},
            {'name': 'Celestial Ruins (Astral)', 'desc': 'Floating spires in low gravity challenge your agility and courage.'},
            {'name': 'Veil of Echoes (Temporal)', 'desc': 'A shifting realm of past and future, where memory is both ally and foe.'},
        ],
        'team': [
            'Gonzalo Fernández Ruiz',
            'Mansi Kadiwala',
            'Mingtao Zhang',
        ],
        'video_demo': 'video/demo.mp4',
        'screenshots': [
            'img/hero.png',
            'img/arena1.png',
            'img/healthBar'
        ],
        'pdf' : 'pdfs/GDD.pdf'
    }
    return render_template('index.html', game=game)

if __name__ == '__main__':
    app.run(debug=True)

# have added the final demo video but need to add this comment to build 