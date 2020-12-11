window.onload = function () {
    document.getElementById("download")
        .addEventListener("click", () => {
            const billetpdf = this.document.getElementById("billetpdf");
            console.log(billetpdf);
            console.log(window);
            var opt = {
                margin: 1,
                filename: 'myfile.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
            };
            html2pdf().from(billetpdf).set(opt).save();
        })
}