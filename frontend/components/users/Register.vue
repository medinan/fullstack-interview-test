<template>
  <div class="main-wrapper">
    <div class="main">
      <div class="main-inner">
        <div class="page-title">
          <div class="container">
            <h1>Register
            </h1>
            <div class="page-title-actions">
              <div class="switcher">
                <strong>Currency</strong>
                <ul>
                  <li class="active"><a href="#">USD</a></li>
                  <li><a href="#">EUR</a></li>
                </ul>
              </div>
              <!-- /.switcher -->
              <div class="switcher">
                <strong>Language</strong>
                <ul>
                  <li class="active"><a href="#">EN</a></li>
                  <li><a href="#">FR</a></li>
                  <li><a href="#">DE</a></li>
                </ul>
              </div>
              <!-- /.switcher -->
            </div>
            <!-- /.page-title-actions -->
          </div>
          <!-- /.container-->
        </div>
        <!-- /.page-title -->
        <div class="container">
          <nav class="breadcrumb">
            <a class="breadcrumb-item" href="#">Home</a>
            <a class="breadcrumb-item" href="#">Library</a>
            <a class="breadcrumb-item" href="#">Data</a>
            <span class="breadcrumb-item active">Bootstrap</span>
          </nav>
          <form method="post">
            <div class="row mb80">
              <div class="col-sm-4 offset-sm-4">
                <h3 class="page-title-small">Register</h3>
                <div class="form-group">
                  <label for="">Username</label>
                  <input type="text" class="form-control">
                </div>
                <!-- /.form-group -->
                <div class="form-group">
                  <label for="">E-mail</label>
                  <input type="mail" class="form-control">
                </div>
                <!-- /.form-group -->
                <div class="form-group">
                  <label for="">Password</label>
                  <input type="password" class="form-control">
                </div>
                <!-- /.form-group -->
                <div class="form-group">
                  <label for="">Retype Password</label>
                  <input type="password" class="form-control">
                </div>
                <!-- /.form-group -->
                <div class="form-group">
                  <label for="">First Name</label>
                  <input type="text" class="form-control">
                </div>
                <!-- /.form-group -->
                <div class="form-group">
                  <label for="">Last Name</label>
                  <input type="text" class="form-control">
                </div>
                <!-- /.form-group -->
                <div class="form-group">
                  <label for="">Address</label>
                  <textarea class="form-control" rows="5"></textarea>
                </div>
                <!-- /.form-group -->
                <div class="center">
                  <div class="checkbox mb30">
                    <label>
                      <div class="checkbox-wrapper"><input type="checkbox"><span class="indicator"></span></div> By signing up, you agree with the <a href="terms-conditions.html">terms and conditions</a>.
                    </label>
                  </div>
                  <!-- /.form-group -->
                  <div class="form-group-btn">
                    <button type="submit" class="btn btn-primary pull-right">Create Account</button>
                  </div>
                  <!-- /.form-group-btn -->
                </div>
                <!-- /.center -->
              </div>
              <!-- /.col-* -->
            </div>
            <!-- /.row -->
          </form>
        </div>
        <!-- /.container-fluid -->
      </div>
      <!-- /.main-inner -->
    </div>
    <!-- /.main -->
  </div>
</template>

<script>
    export default {
        name: "Register"
    }
</script>

<style scoped>

</style>
