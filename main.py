from flask import Flask, render_template, request
# import downloadDB

app = Flask(__name__)

# Creates route (url)
@app.route("/")
def main():
    # Get list of pokemon from database.
    pokemonList = []
    return render_template("index.html", pokemonList=pokemonList)

@app.route("/downloadPokemon")
def downloadPokemonData():
    # downloaded = downloadDB.downloadPokemonData()
    return main()

@app.route("/pokemonCard")
def produceCard():
    args=request.args
    # download data (Isaac)
    print(args["pokemonList"])
    return render_template("pokemonCard.html", pokemonCard=["Poke1", "Poke2", "Poke3"])

if __name__ == '__main__':
    app.run()