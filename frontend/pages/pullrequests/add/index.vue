<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <PullRequestAdd></PullRequestAdd>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';
import PullRequestAdd from "~/components/pullrequests/pullrequest-add";

export default {
  components: {
    Logo, Menu, Footer, PullRequestAdd
  }
}
</script>

<style>
</style>
