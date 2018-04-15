new Vue({
  el: '#app',
  data: {
    items: [],
    paginate: ['items']
  },
  created: function () {
    this.$http.get('api/items/')
      .then(response => {
          // Define url
          this.items = response.data;
      });
  },
  methods: {
    onSelectItem: function (item) {
        console.log(item);
    },
    removeRow: function (item) {
      for(var i = this.items.length - 1; i >= 0; i--) {
        if(this.items[i].id === item.id) {
           this.items.splice(i, 1);
           break;
        }
      }
      this.$http.delete('api/items/'+item.id)
      .then(response => {
          console.log("remove");
      });
        
    },
  }
})