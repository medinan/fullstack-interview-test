<template>
  <div class="col-md-4 col-lg-4">
    <div class="listing-row">
      <div class="listing-box-inner">
        <a class="listing-box-image" :href="link_detail">
          <span class="listing-box-image-content" v-bind:style="'background-image: url('+ image_url +')'"></span>
        </a>
        <div class="listing-row-content">
          <div class="listing-row-content-header">
            <h3><a href="listings-detail.html">{{ name }}</a></h3>
            <h4> {{ address }}</h4>
            <div class="actions">
              <div class="actions-button">
                <span></span>
                <span></span>
                <span></span>
              </div>
              <!-- /.actions-button -->
              <ul class="actions-list">
                <li><a href="#">Favoritos</a></li>
              </ul>
              <!-- /.actions-list -->
            </div>
            <!-- /.actions -->
          </div>
          <!-- /.listing-row-content-header -->
          <div class="listing-row-content-meta">
            <div class="listing-row-content-meta-item listing-row-content-meta-rating">
                            <span class="listing-row-rating">
                              <i class="fa fa-star"></i>
                              <i class="fa fa-star"></i>
                              <i class="fa fa-star"></i>
                              <i class="fa fa-star"></i>
                              <i class="fa fa-star"></i>
                            </span>
            </div>
            <!-- /.listing-row-meta-item -->

            <div class="listing-row-content-meta-item listing-row-content-meta-category">
              <span class="tag">{{ category }}</span>
            </div>
            <!-- /.listing-row-meta-item -->
          </div>
          <!-- /.listing-row-meta-item -->
          <div class="listing-row-content-body">
            {{ description }}
            <div class="listing-row-content-read-more">
              <a class="btn" :href="link_detail">Ver más</a>
            </div>
            <!-- /.listing-row-content-read-more -->
          </div>
          <!-- /.listing-row-content-body -->
        </div>
        <!-- /.listing-row-content -->
      </div>
      <!-- /.listing-row-inner -->
    </div>
  </div>
</template>

<script>
    export default {
        name: "premium",
        props: ['name', 'address', 'category', 'description', 'link_detail', 'image_url']
    }
</script>

<style scoped>
  .listing-row-image {
    min-width: 300px;
  }
  .listing-row-content-read-more .btn {
    background-color: #F74949;
    color: #fff;
  }
</style>
