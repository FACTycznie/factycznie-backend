
import { FontAwesomeIcon, FontAwesomeLayers } from '@fortawesome/vue-fontawesome'

let noneString = "BRAK";

let unknown = 0,
  loading = 1,
  checkedTrue = 2,
  checkedFalse = 3;

let unknownIconClass = "fas fa-question-circle criteria-unknown",
  loadingIconClass = "fas fa-spinner fa-pulse criteria-spinner",
  falseIconClass = "fas fa-times criteria-false",
  trueIconClass = "fas fa-check criteria-true";

let sourceRelevanceUnknown = 0,
  sourceRelevanceUncertain = 1,
  sourceRelevanceSoso = 2,
  sourceRelevanceTrusted = 3;
// "NIEZNANE ŹRÓDŁO", "NIEPEWNE ŹRÓDŁO", "PRZYZWOITE ŹRÓDŁO", "ZAUFANE ŹRÓDŁO"
// "Brak danych w systemie na temat podanego źródła."
// "News, który sprawdzasz pochodzi z portalu, na którym można znaleźć fake-newsy lub clickbaity (wniosek na podstawie [X] przeanalizowanych newsów).
// "News, który sprawdzasz pochodzi z portalu, który przeważnie zawiera wiarygodne informacje, jednak można na nim czasem znaleźć artykuły o wątpliwej jakości (wniosek na podstawie [X] przeanalizowanych newsów).
// "News, który sprawdzasz pochodzi z portalu, który oceniany jest jako źródło wiarygodnych informacji (wniosek na podstawie [X] przeanalizowanych newsów).

let clickbaitsNone = 0,
  clickbaitsFew = 1,
  clickbaitsPlenty = 2;

let scrollOptions = {
    // container: '#container',
    easing: 'ease-in',
    offset: -90,
    cancelable: true,
    onDone: function() {
      // scrolling is done
    },
    onCancel: function() {
      // scrolling has been interrupted
    },
    x: false,
    y: true
}

let authorState = unknown;

let vm = new Vue({
  el: '#container',
  // components: {
  //   FontAwesomeIcon,
  //   FontAwesomeLayers
  // },
  delimiters: ['[[', ']]'],
  data: {
    searchURL: "",
    loading: false,
    showAnalysis: false,

    authorState: unknown,
    newsAuthorDecision: noneString,

    sourceRelevanceState: unknown,
    sourceRelevance: sourceRelevanceUnknown,

    similarNewsState: unknown,
    similarNewsDecision: noneString,
    // <span id="criteria-no-similar">BRAK</span></strong><span id="criteria-found-similar">Znaleziono portale, które napisały na podobny temat:</span>
    similarNewsList: [],

    analyzedHeader: null,
    analyzedBody: null,

    clickbaitsState: unknown,
    clickbaitsDecision: noneString,
    clickbaitsString: noneString
  },
  computed: {
    authorIcon: function () {
      switch (this.authorState) {
        case unknown:
          return unknownIconClass;
        case loading:
          return loadingIconClass;
        case checkedTrue:
          return trueIconClass;
        case checkedFalse:
          return falseIconClass;
      }
    },
    sourceRelevanceStateIcon: function () {
      switch (this.sourceRelevanceState) {
        case unknown:
          return unknownIconClass;
        case loading:
          return loadingIconClass;
        case checkedTrue:
          return trueIconClass;
        case checkedFalse:
          return falseIconClass;
      }
    },
    similarNewsStateIcon: function () {
      switch (this.similarNewsState) {
        case unknown:
          return unknownIconClass;
        case loading:
          return loadingIconClass;
        case checkedTrue:
          return trueIconClass;
        case checkedFalse:
          return falseIconClass;
      }
    },
    clickbaitsStateIcon: function () {
      switch (this.clickbaitsState) {
        case unknown:
          return unknownIconClass;
        case loading:
          return loadingIconClass;
        case checkedTrue:
          return trueIconClass;
        case checkedFalse:
          return falseIconClass;
      }
    }
  },
  methods: {
    factCheck: function(url) {
      this.authorState = this.sourceRelevanceState = this.similarNewsState = this.clickbaitsState = loading;
      this.loading = true;
      this.showAnalysis = true;

      let params = null;
      if (url !== null) {
        params = {
          url: url
        };
      }

      this.$http
      .get('/api/document/evaluation', {params: params}).then(function (response) {
        let container = this.$el.querySelector("#fact-analysis");
        // let navbarHeight = this.$refs.factNavbar.clientHeight;
        // scrollOptions.offset = - navbarHeight;
        cancelScroll = this.$scrollTo(container, 400, scrollOptions);

        this.analyzedHeader = response.body.title;
        this.analyzedBody = response.body.text;

        console.log(response.body);
        if (response.body.authors_score > 0) {
          this.authorState = checkedTrue;
        }
        else {
          this.authorState = checkedFalse;
          this.newsAuthorDecision = noneString;
        }

        this.loading = false;
      });
    },
    factCheckNoURL: function () {
      this.factCheck();
    },
    factCheckURL: function (e) {
      e.preventDefault();
      this.factCheck(this.searchURL);
    }
  }
})
