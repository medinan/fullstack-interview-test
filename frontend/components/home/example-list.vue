<template>
  <div class="main-wrapper">
    <div class="main">
      <div class="main-inner">
        <div class="page-header">
          <h2>Encontrá todo lo que necesitás para tu evento</h2>
          <p>¡Tenemos cientos de proveedores en los mas diversos rubros!.</p>
        </div>
        <div class="container">
          <div class="content">
            <div class="row" >
              <premium-card v-for="adv in advertisements"
                            :name="adv.name"
                            :address="adv.address"
                            :description="adv.description"
                            :category="adv.category"
                            :image_url="adv.image_url"
              >

              </premium-card>
            </div>
          </div>

        </div>


        <!-- /.container-fluid -->
      </div>
      <!-- /.main-inner -->
    </div>
    <!-- /.main -->
  </div>
</template>

<script>
    import PremiumCard from '~/components/cards/premium.vue';
    import CarouselBanners from '~/components/home/carousel-banners.vue';

    export default {
        name: "example-list",
        components: {PremiumCard, CarouselBanners},
        data(){
            return {
                advertisements: [
                    {
                        'id': 1,
                        'name': 'La paloma eventos',
                        'type': 'PREMIUM',
                        'category': 'Salones de fiesta',
                        'description': 'El salón Ranelagh IV es uno de nuestros salones más nuevos y se encuentra en la ' +
                            'ciudad de Berazategui, en Av. Valentín Vergara N° 5520. ' +
                            'Capacidad: 160 personas. Recepción Amueblada con Puff y sillones. ' +
                            'Salón Central con Pista de Baile.',
                        'image_url': '/img/example/cards/salon_1.jpg',
                        'address': 'Calle 9 4608, B1880 Berazategui, Buenos Aires'
                    },
                    {
                        'id': 2,
                        'name': 'La paloma eventos',
                        'type': 'PREMIUM',
                        'category': 'Salones de fiesta',
                        'description': 'El salón Ranelagh IV es uno de nuestros salones más nuevos y se encuentra en la ' +
                            'ciudad de Berazategui, en Av. Valentín Vergara N° 5520. ' +
                            'Capacidad: 160 personas. Recepción Amueblada con Puff y sillones. ' +
                            'Salón Central con Pista de Baile.',
                        'image_url': '/img/example/cards/salon_1.jpg',
                        'address': 'Calle 9 4608, B1880 Berazategui, Buenos Aires'
                    },
                    {
                        'id': 3,
                        'name': 'La paloma eventos',
                        'type': 'PREMIUM',
                        'category': 'Salones de fiesta',
                        'description': 'El salón Ranelagh IV es uno de nuestros salones más nuevos y se encuentra en la ' +
                            'ciudad de Berazategui, en Av. Valentín Vergara N° 5520. ' +
                            'Capacidad: 160 personas. Recepción Amueblada con Puff y sillones. ' +
                            'Salón Central con Pista de Baile.',
                        'image_url': '/img/example/cards/salon_1.jpg',
                        'address': 'Calle 9 4608, B1880 Berazategui, Buenos Aires'
                    },
                    {
                        'id': 4,
                        'name': 'La paloma eventos',
                        'type': 'PREMIUM',
                        'category': 'Salones de fiesta',
                        'description': 'El salón Ranelagh IV es uno de nuestros salones más nuevos y se encuentra en la ' +
                            'ciudad de Berazategui, en Av. Valentín Vergara N° 5520. ' +
                            'Capacidad: 160 personas. Recepción Amueblada con Puff y sillones. ' +
                            'Salón Central con Pista de Baile.',
                        'image_url': '/img/example/cards/salon_1.jpg',
                        'address': 'Calle 9 4608, B1880 Berazategui, Buenos Aires'
                    },
                ]
            }
        }
    }
</script>

<style scoped>

</style>
