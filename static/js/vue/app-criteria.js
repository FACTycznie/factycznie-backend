
var unknown = 0, loading = 1, checkedTrue = 2, checkedFalse = 3;

var vm = new Vue({
  el: '#factycznie-criteria',
  delimiters: ['[[', ']]'],
  data: {
    criteria: [
      { id: 0, verification: unknown, expanded: false },
      { id: 1, verification: unknown, expanded: false },
      { id: 2, verification: unknown, expanded: false },
      { id: 3, verification: unknown, expanded: false }
    ],
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
})

Vue.component('criteria-item', {
  // The todo-item component now accepts a
  // "prop", which is like a custom attribute.
  // This prop is called todo.
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})