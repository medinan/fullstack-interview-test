<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <PullRequesList></PullRequesList>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';
import PullRequesList from "~/components/pullrequests/pullrequest-list";

export default {
  components: {
    Logo, Menu, Footer, PullRequesList
  }
}
</script>

<style>
</style>
