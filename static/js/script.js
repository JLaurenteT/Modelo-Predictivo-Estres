document.getElementById('formulario').addEventListener('submit', async (e) => {
  e.preventDefault();

  const datos = Object.fromEntries(new FormData(e.target).entries());

  const response = await fetch('/predecir', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(datos)
  });

  const result = await response.json();
  const resultado = document.getElementById('resultado');

  if (result.categoria_estres) {
    resultado.textContent = `Nivel de Estrés: ${result.categoria_estres}`;
    resultado.classList.remove('text-danger');
    resultado.classList.add('text-primary');
  } else {
    resultado.textContent = `Error: ${result.error}`;
    resultado.classList.remove('text-primary');
    resultado.classList.add('text-danger');
  }
});
