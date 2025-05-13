fetch("/api/data")
  .then(response => response.json())
  .then(data => {
    const table = document.createElement("table");
    if (data.length > 0) {
      const header = table.insertRow();
      Object.keys(data[0]).forEach(key => {
        const cell = header.insertCell();
        cell.innerHTML = `<strong>${key}</strong>`;
      });

      data.forEach(row => {
        const rowElement = table.insertRow();
        Object.values(row).forEach(value => {
          const cell = rowElement.insertCell();
          cell.textContent = value;
        });
      });
    }
    document.getElementById("data-table").appendChild(table);
  });
