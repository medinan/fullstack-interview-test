<template>
  <div class="footer-wrapper">
    <div class="footer">
      <div class="footer-inner">
        <div class="container">
          <div class="row">
            <div class="col-lg-4">
              <div class="widget">
                <h3>
                  <img v-bind:src="require('../assets/img/layer105.png')" alt="Home">
                </h3>
                <p>
                  WEB Y EVENTOS es un sitio de servicios de información publicitaria.
                  No tiene relación alguna con las operaciones comerciales que se realicen directamente
                  entre usuarios y anunciantes. La fidelidad de los datos presentados en cada anuncio es
                  responsabilidad exclusiva de los anunciantes.
                </p>
                <ul class="social">
                  <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                  <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                  <li><a href="#"><i class="fa fa-google"></i></a></li>
                </ul>
              </div>
            </div>
            <!-- /.col-* -->
            <div class="col-lg-4 header-light">
              <div class="widget">
                <ul class="nav nav-pills">
                  <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
                  <li class="nav-item"><a class="nav-link" href="index-classified.html">Organiza tu fiesta</a></li>
                  <li class="nav-item"><a class="nav-link" href="index-job-board.html">Ingresá</a></li>
                  <li class="nav-item"><a class="nav-link" href="index-real-estate.html">Regístrate</a></li>
                  <li class="nav-item"><a class="nav-link" href="index-automotive.html">Anunciantes</a></li>
                  <li class="nav-item"><a class="nav-link" href="index-travel.html">Terminos y condiciones</a></li>
                  <li class="nav-item"><a class="nav-link" href="index-travel.html">Todas nuestras categorias</a></li>
                  <li class="nav-item"><a class="nav-link" href="index-restaurant.html">Ayuda</a></li>
                </ul>
              </div>
              <!-- /.widget -->
            </div>
            <!-- /.col-* -->
            <div class="col-lg-4">
              <div class="widget">
                <h3>Todas las en tu email</h3>
                <p>
                  Recibe en tu correo electrónico todas nuestras ofertas y novedades en tu email.
                </p>
                <form method="post">
                  <div class="form-group">
                    <input type="email" class="form-control" placeholder="Your e-mail address">
                  </div>
                  <!-- /.form-group -->
                  <div class="form-group clearfix">
                    <button type="submit" class="btn btn-primary pull-right">Suscríbete</button>
                  </div>
                  <!-- /.form-group -->
                </form>
              </div>
              <!-- /.widget -->
            </div>
            <!-- /.col-* -->
          </div>
          <!-- /.row -->
        </div>
        <!-- /.container -->
      </div>
      <!-- /.footer-inner -->
    </div>
    <!-- /.footer -->
  </div>
</template>

<script>
    export default {
        name: "footer"
    }
</script>

<style scoped>

</style>
