
$(function () {


  // =====================================
  // Profit
  // =====================================

  var select = document.getElementById('razones');
  var chartDiv = document.getElementById('chart');

  // Agregar un listener para el evento de cambio
  select.addEventListener('change', function () {
    // Obtener el valor seleccionado
    var valorSeleccionado = select.value;

    if (valorSeleccionado == 1) {
      chartDiv.innerHTML = "";

      graficoBarras('factor', [["Dificultades", "económicas"], ["Problemas personales/", "familiares"], ["Falta de interés en el", " programa de formación"], ["Falta de apoyo", "académico"], ["Oportunidades laborales", "externas"]]);
    }
    if (valorSeleccionado == 2) {
      chartDiv.innerHTML = "";
      graficodEdades('edad', ["Adulto", "Joven", "Adolescente"]);
    }
    if (valorSeleccionado == 3) {
      chartDiv.innerHTML = "";
      graficoBarrasColores();
    }
    if (valorSeleccionado == 4) {
      chartDiv.innerHTML = "";
      chartDiv.removeAttribute("style");
    }
  });

  // Llamar a la función para cargar el gráfico al inicio
  graficoBarras('factor', [["Dificultades", "económicas"], ["Problemas personales/", "familiares"], ["Falta de interés en el", " programa de formación"], ["Falta de apoyo", "académico"], ["Oportunidades laborales", "externas"]]);


  function graficoBarras(nombreOpcion, categorias) {
    var vector = JSON.parse(document.getElementById(nombreOpcion).getAttribute('data-vector'));

    var chart = {
      series: [
        { name: "", data: vector },
      ],

      chart: {
        type: "bar",
        height: 345,
        offsetX: -15,
        toolbar: { show: true },
        foreColor: "#000",
        fontFamily: 'inherit',
        sparkline: { enabled: false },
      },

      colors: ["#39a900"],

      plotOptions: {
        bar: {
          horizontal: false,
          columnWidth: "35%",
          borderRadius: [6],
          borderRadiusApplication: 'end',
          borderRadiusWhenStacked: 'all'
        },
      },

      dataLabels: {
        enabled: true,
      },

      xaxis: {
        type: "category",
        categories: categorias,
      },

      yaxis: {
        show: true,
        min: 0,
        max: Math.ceil(Math.max(...vector) / 10) * 10,
        tickAmount: 4,
      },

      stroke: {
        show: true,
        width: 3,
        lineCap: "butt",
        colors: ["transparent"],
      },

      tooltip: { theme: "light" },

      responsive: [
        {
          breakpoint: 600,
          options: {
            plotOptions: {
              bar: {
                borderRadius: 3,
              }
            },
          }
        }
      ]

    };

    var chart = new ApexCharts(document.querySelector("#chart"), chart);
    chart.render();
  }

  //=======================================
  //Grafico de edades
  //======================================
  function graficodEdades(nombreOpcion, categorias) {
    var vector = JSON.parse(document.getElementById(nombreOpcion).getAttribute('data-vector'));
    var options = {
      series: [{
        data: vector
      }],
      chart: {
        type: 'bar',
        height: 345
      },
      plotOptions: {
        bar: {
          borderRadius: 4,
          horizontal: true,
        }
      },
      dataLabels: {
        enabled: false
      },
      xaxis: {
        categories: categorias,
      }
    };

    var chart = new ApexCharts(document.querySelector("#chart"), options);
    chart.render();

  }

  //=======================================
  //Grafico barras de colores
  //======================================

  function graficoBarrasColores() {
    var colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33F6', '#F6FF33', '#33F6FF', '#A633FF', '#FF33A6'];

    var vector = JSON.parse(document.getElementById('tecnologica').getAttribute('data-vector'));

    var categorias = [
      ['Analisis', 'y Desarrollo', 'de Software'],
      ['Animacion', 'Digital'],
      ['Automatizacion', 'de Sistemas', 'Mecatronicos'],
      ['Desarrollo', 'de Productos', 'Electronicos'],
      ['Desarrollo', 'de Sistemas', 'Electronicos Industriales'],
      ['Diseno', 'e Integracion', 'de Automatismos', 'Mecatronicos'],
      ['Gestion', 'de la Produccion', 'Industrial'],
      ['Gestion Integral', 'del Transporte'],
      ['Implementacion', 'de Infraestructura', 'de Tecnologias', 'de la Informacion', 'y las Comunicaciones'],
      ['Implementacion', 'de Redes', 'y Servicios', 'de Telecomunicaciones'],
      ['Mantenimiento', 'de Equipo', 'Biomedico'],
      ['Produccion', 'de Componentes', 'Mecanicos', 'con Maquinas', 'de Control', 'Numerico Computarizado']
    ]


    var options = {
      series: [{
        data: vector
      }],
      chart: {
        height: 345,
        type: 'bar',
        events: {
          click: function (chart, w, e) {
            // console.log(chart, w, e)
          }
        }
      },
      colors: colors,
      plotOptions: {
        bar: {
          columnWidth: '45%',
          distributed: true,
        }
      },
      dataLabels: {
        enabled: false
      },
      legend: {
        show: true
      },
      xaxis: {
        categories: categorias,
        labels: {
          show: false,
          style: {
            colors: colors,
            fontSize: '12px'
          }
        }
      }
    };

    var chart = new ApexCharts(document.querySelector("#chart"), options);
    chart.render();
  }

  // =====================================
  // Breakup
  // =====================================
  var breakup = {
    color: "#adb5bd",
    series: [parseInt(document.getElementById('cancelado').getAttribute('data-info')), parseInt(document.getElementById('retirado').getAttribute('data-info'))],
    labels: ["Cancelado", "Retiro voluntario"],
    chart: {
      width: 180,
      type: "donut",
      fontFamily: "Plus Jakarta Sans', sans-serif",
      foreColor: "#adb0bb",
    },
    plotOptions: {
      pie: {
        startAngle: 0,
        endAngle: 360,
        donut: {
          size: '75%',
        },
      },
    },
    stroke: {
      show: false,
    },

    dataLabels: {
      enabled: false,
    },

    legend: {
      show: false,
    },
    colors: ["#FF0000", "#808080"],

    responsive: [
      {
        breakpoint: 991,
        options: {
          chart: {
            width: 150,
          },
        },
      },
    ],
    tooltip: {
      theme: "dark",
      fillSeriesColor: false,
    },
  };

  var breakup = new ApexCharts(document.querySelector("#breakup"), breakup);
  breakup.render();



  // =====================================
  // Earning
  // =====================================
  var vector = JSON.parse(document.getElementById('frecuencia').getAttribute('data-vector'));
  console.log("Vector: ", vector)
  var earning = {
    chart: {
      id: "sparkline3",
      type: "area",
      height: 200,
      sparkline: {
        enabled: false,
      },
      fontFamily: "Plus Jakarta Sans', sans-serif",
      foreColor: "#000",
      toolbar: {
        show: false,
      },
    },
    series: [
      {
        name: "Deserciones",
        color: "#49BEFF",
        data: vector,
      },
    ],

    stroke: {
      curve: "smooth",
      width: 2,
      dashArray: [0], // This will hide the data points on the chart
      markers: {
        size: 0,
      },
    },
    markers: {
      size: 0,
    },

    tooltip: {
      theme: "dark",
      fixed: {
        enabled: true,
        position: "right",
      },
      x: {
        show: false,
      },
    },
    xaxis: {
      categories: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"], // Meses del año como etiquetas del eje X
    },
    yaxis: {
      show: false,
    },
  };

  new ApexCharts(document.querySelector("#earning"), earning).render();

  // =====================================
  // Hombres vs mujeres
  // =====================================
  var vector = JSON.parse(document.getElementById('hombresvsmujeres').getAttribute('data-vector'));
  var hombresvsmujeres = {
    series: vector,
    chart: {
      width: 250,
      type: 'pie',
    },
    labels: ['Masculino', 'Femenino'],
    colors: ["#0084d2", "#ff6070"],
    dataLabels: {
      style: {
        colors: ["#000000"] // Color del texto en porcentaje (en este caso, negro)
      }
    },
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

  var hombresvsmujeres = new ApexCharts(document.querySelector("#hombresvsmujeres"), hombresvsmujeres);
  hombresvsmujeres.render();
  // =====================================
  // tecnologo vs tecnicos
  // =====================================
  var vector = JSON.parse(document.getElementById('niveldeformacion').getAttribute('data-vector'));

  var nivelDeFormacion = {
    series: vector,
    chart: {
      type: 'donut',
      width: 250,
    },
    labels: ['Técnico', 'Tecnólogo'],
    colors: ["#FFA500", "#1E90FF"],
    dataLabels: {
      style: {
        colors: ["#000000"] // Color del texto en porcentaje (en este caso, negro)
      }
    },

    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

  var nivelDeFormacion = new ApexCharts(document.querySelector("#niveldeformacion"), nivelDeFormacion);
  nivelDeFormacion.render();

  // =====================================
  // retencion
  // =====================================
  var vector = JSON.parse(document.getElementById('retencionvsdesercion').getAttribute('data-vector'));

  var retencionVsDesercion = {
    series: vector,
    chart: {
      type: 'donut',
      width: 500,
    },
    labels: ['Retención', 'Deserción'],
    colors: ["#39a900", "#FF0000"],
   
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

  var retencionVsDesercion = new ApexCharts(document.querySelector("#retencionvsdesercion"), retencionVsDesercion);
  retencionVsDesercion.render();

  // =====================================
  // Permanencia por trimestres
  // =====================================
  var vector = JSON.parse(document.getElementById('permanencia').getAttribute('data-vector'));

  var permanencia = {
    series: [{
      name: 'Total aprendices',
      type: 'column',
      data: vector[1]
    }, {
      name: 'Permanencia',
      type: 'line',
      data: vector[0]
    }],
    chart: {
      height: 350,
      width: 500,
      type: 'line',
      fontFamily: "Plus Jakarta Sans', sans-serif",
      foreColor: "#000",
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "50%",
        borderRadius: [6],
        borderRadiusApplication: 'end',
        borderRadiusWhenStacked: 'all'
      },
    },
    stroke: {
      width: [0, 4]
    },

    dataLabels: {
      enabled: true,
      enabledOnSeries: [1]
    },
    labels: ['Trimestre 1', 'Trimestre 2', 'Trimestre 3', 'Trimestre 4'],

    yaxis: [{
      title: {
        text: 'Total aprendices',
      },

    }, {
      opposite: true,
      title: {
        text: 'Permanencia'
      }
    }]
  };

  var permanencia = new ApexCharts(document.querySelector("#permanencia"), permanencia);
  permanencia.render();


})