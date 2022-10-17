from flask import Flask, render_template, request
# import downloadDB

app = Flask(__name__)

@app.route("/")

def main():
    # Get list of pokemon from database.
    return render_template("index.html", #downloaded message)

@app.route("/downloadPokemon")
def downloadPokemonData():
    # download data (Isaac)
    # downloaded = downloadDB.downloadPokemonData()
    # if downloaded == True:
    # If downloaded add 'downloaded msg'
    # If not, not.
    # return main()

@app.route("/pokemonCard/<pokemonName>")
def produceCard(pokemonName):
    # download data (Isaac)
    return render_template("pokemonCard.html", pokemonCard=["Poke1", "Poke2", "Poke3"])

if __name__ == '__main__':
    app.run()