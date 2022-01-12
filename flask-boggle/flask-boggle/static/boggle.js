class BoggleGame {
    constructor (boardId, secs = 60) {
        this.secs = secs;
        this.showTimer();

        this.score = 0;
        this.words = new Set();
        this.board = $('#' + boardId);
    }
  showWord(word) {
    $(".words", this.board).append($("<li>", {text:word}));
    /*this will create a new li element to display the new word
    that was input*/
  }

  showScore() {
      $(".score", this.board).text(this.score);
      //will display the current score
  }

  showMessage(msg, cls) {
      $(".msg", this.board).text(msg).removeClass().addClass(`msg ${cls}`);
      //will display status messages
  }


async handleSubmit(evt) {
    evt.preventDefault();
    //event does not get explicitly handled or go to another site
    const $word = $(".word", this.board)

    let word = $word.val();
    if(!word) return;
    //so if not a word return with error
    //now we need to relay msg for duplicates
    if (this.words.has(word)) {
        this.showMessage(`Already found ${word}`, "err")
        return;
     }
    }

    //check server for validity
    const resp = await axios.get("/check-word", {params: {word:word}});
    

}