<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <ImageHero></ImageHero>
    <ExampleList></ExampleList>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import ImageHero from '~/components/home/image-hero.vue';
import ExampleList from '~/components/home/example-list.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';

export default {
  components: {
    Logo, Menu, ImageHero, Footer, ExampleList
  }
}
</script>

<style>
</style>
