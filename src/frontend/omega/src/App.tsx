import { useEffect } from 'react';
import Highcharts from 'highcharts';

function App() {
  useEffect(() => {
    // Gráfico de evolução dos modelos
    Highcharts.chart('model-evolution', {
      chart: {
        type: 'line',
        backgroundColor: 'transparent',
        style: {
          fontFamily: 'system-ui, -apple-system, sans-serif'
        }
      },
      title: {
        text: 'Evolução dos Modelos Omega',
        style: { color: '#FFFFFF' }
      },
      xAxis: {
        categories: ['Omega 1B', 'Omega 2B', 'Omega 3B'],
        labels: { style: { color: '#9CA3AF' } },
        lineColor: 'rgba(255, 255, 255, 0.1)'
      },
      yAxis: {
        title: {
          text: 'Taxa de Acerto (%)',
          style: { color: '#9CA3AF' }
        },
        labels: { style: { color: '#9CA3AF' } },
        gridLineColor: 'rgba(255, 255, 255, 0.1)'
      },
      series: [{
        type: 'line',
        name: 'Raciocínio Lógico',
        data: [45, 68, 89],
        color: '#8B5CF6'
      }, {
        type: 'line',
        name: 'Compreensão de Contexto',
        data: [30, 75, 92],
        color: '#D946EF'
      }, {
        type: 'line',
        name: 'Resolução de Problemas',
        data: [38, 72, 88],
        color: '#EC4899'
      }],
      legend: {
        itemStyle: { color: '#9CA3AF' },
        itemHoverStyle: { color: '#FFFFFF' }
      },
      plotOptions: {
        line: {
          marker: {
            enabled: true,
            symbol: 'circle',
            radius: 6
          }
        }
      },
      credits: {
        enabled: false
      }
    });
  }, []);

  return (
    <div>
      {/* Background dots */}
      <div className="floating-dots">
        {[...Array(20)].map((_, i) => (
          <div
            key={i}
            className="dot"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 5}s`
            }}
          />
        ))}
      </div>

      <nav className="navbar">
        <div className="container">
          <div className="navbar-content">
            <a className="logo">Omega AI</a>
            <div className="nav-buttons">
              <button className="btn btn-ghost">Login</button>
              <button className="btn btn-primary">
                Começar
                <i className="fas fa-arrow-right"></i>
              </button>
            </div>
          </div>
        </div>
      </nav>

      <main>
        <section className="hero">
          <div className="container">
            <div className="hero-content">
              <div className="hero-text">
                <h1 className="hero-title">
                  <span className="typing-text">Seu Computador</span>
                  <span className="hero-gradient-text">Mais Inteligente</span>
                </h1>
                <br />
                <p className="hero-subtitle">
                  Automatize tarefas e otimize seu sistema com IA avançada e recursos inteligentes
                </p>
                <div className="nav-buttons">
                  <button className="btn btn-primary">
                    <span>Instalar Agora</span>
                    <i className="fas fa-download"></i>
                  </button>
                  <button className="btn btn-ghost">
                    Ver Demo
                  </button>
                </div>
                
                <div className="stats">
                  <div>
                    <div className="stat-value">98%</div>
                    <div className="stat-label">Satisfação</div>
                  </div>
                  <div>
                    <div className="stat-value">24/7</div>
                    <div className="stat-label">Suporte</div>
                  </div>
                  <div>
                    <div className="stat-value">+50k</div>
                    <div className="stat-label">Usuários</div>
                  </div>
                </div>
              </div>
              
              <div className="hero-image">
                <div className="animate-pulse"></div>
                <img 
                  src="/hero-image.svg" 
                  alt="IA Interface" 
                />
              </div>
            </div>
          </div>
        </section>

        <section className="evolution">
          <div className="container">
            <div className="section-header">
              <h2 className="section-title">
                Evolução Constante
              </h2>
              <p className="section-description">
                Acompanhe o progresso dos nossos modelos de IA em diferentes aspectos
              </p>
            </div>
            <div id="model-evolution" className="chart-container"></div>
          </div>
        </section>

        <section className="features">
          <div className="container">
            <div className="section-header">
              <h2 className="section-title">
                O que a Omega AI faz no seu computador
              </h2>
              <p className="section-description">
                Uma plataforma completa de automação e otimização para seu sistema
              </p>
            </div>
            
            <div className="features-grid">
              <div className="feature-card">
                <div className="feature-icon">
                  <i className="fas fa-folder-open"></i>
                </div>
                <h3 className="feature-title">Organiza Arquivos</h3>
                <p className="feature-description">
                  Classifica e organiza automaticamente seus documentos de forma inteligente
                </p>
              </div>

              <div className="feature-card">
                <div className="feature-icon">
                  <i className="fas fa-tachometer-alt"></i>
                </div>
                <h3 className="feature-title">Otimiza Desempenho</h3>
                <p className="feature-description">
                  Monitora e melhora a performance do seu sistema em tempo real
                </p>
              </div>

              <div className="feature-card">
                <div className="feature-icon">
                  <i className="fas fa-shield-alt"></i>
                </div>
                <h3 className="feature-title">Backup Inteligente</h3>
                <p className="feature-description">
                  Identifica e protege seus arquivos importantes automaticamente
                </p>
              </div>

              <div className="feature-card">
                <div className="feature-icon">
                  <i className="fas fa-robot"></i>
                </div>
                <h3 className="feature-title">Assistente Virtual</h3>
                <p className="feature-description">
                  Ajuda em tarefas diárias com automação inteligente
                </p>
              </div>
            </div>
          </div>
        </section>

        <section className="compatibility">
          <div className="container">
            <div className="section-header">
              <h3 className="section-title">
                Compatível com todos os sistemas
              </h3>
              <p className="section-description">
                Funciona perfeitamente em qualquer sistema operacional
              </p>
            </div>
            
            <div className="os-grid">
              <div className="os-card">
                <i className="fab fa-windows os-icon"></i>
                <span>Windows 10/11</span>
              </div>
              <div className="os-card">
                <i className="fab fa-apple os-icon"></i>
                <span>macOS 12+</span>
              </div>
              <div className="os-card">
                <i className="fab fa-linux os-icon"></i>
                <span>Ubuntu 20.04+</span>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  )
}

export default App
