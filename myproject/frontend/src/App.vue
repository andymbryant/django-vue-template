<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vue Frontend</span>
        <span class="font-weight-light">&nbsp;Django Backend</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-content>
      <Posts/>
    </v-content>
  </v-app>
</template>

<script>
import Posts from "./components/Posts";

export default {
  name: "App",
  components: {
    Posts
  },
  data() {
    return {};
  }
};
</script>
