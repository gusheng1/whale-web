<template>
  <v-container>
    <v-list
      subheader
      two-line
    >
      <v-subheader inset>Recent Articles</v-subheader>

      <v-list-item
        v-for="item in articles"
        :key="item.id"
      >
        <v-list-item-avatar>
          <v-icon
            class="grey lighten-1"
            dark
          >
            mdi-account-circle
          </v-icon>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>
            {{item.title}}
          </v-list-item-title>

          <v-list-item-subtitle v-text="item.created_at"></v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
          <v-btn icon :to="`/articles/detail/${item.id}`">
            <v-icon color="grey lighten-1">mdi-information</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-container>
</template>


<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-list>
      <v-list-item-group v-model="model">
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>


<script>
export default {
  name: 'ArticleList',
  data() {
    return {
      articles: [],
    };
  },
  mounted() {
    this.$axios.get('/articles').then((data) => {
      this.articles = data.data;
    });
  },
};
</script>



