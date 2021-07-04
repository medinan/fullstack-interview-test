<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <Register></Register>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';
import Register from "~/components/users/Register";

export default {
  components: {
    Logo, Menu, Footer, Register
  }
}
</script>

<style>
</style>
