<template>
  <div class="header-wrapper header-light affix-top">
      <div class="header">
        <div class="container">
          <div class="header-inner">
            <div class="navigation-toggle toggle">
              <span></span>
              <span></span>
              <span></span>
            </div>
            <div class="header-logo">
              <a href="index.html">
                <img v-bind:src="require('../assets/img/logo-white.svg')" alt="Home">
              </a>
            </div>
            <div class="header-nav">
              <div class="primary-nav-wrapper">
                <ul class="nav">
                  <li class="nav-item">
                    <a href="#" class="nav-link active">Branches</a>
                  </li>
                  <li class="nav-item">
                    <a href="#" class="nav-link active">Pull request</a>
                  </li>
                </ul>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "menu",
        data () {
          return {

          }
        },
        mounted() {
            $('.navigation-toggle').on('click', function(e) {
                e.preventDefault();
                $('body').toggleClass('navigation-open');
            });
        }
    }
</script>

<style scoped>
  .header-wrapper {
    background: rgba(12, 12, 12, 0.75);
  }
</style>
