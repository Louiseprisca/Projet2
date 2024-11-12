const destinations = {
    yaounde: {
        title: "Yaoundé",
        description: "La capitale politique",
        prix_eco: 4000,
        prix_business: 10000
    },
    douala: {
        title: "Douala",
        description: "La capitale economique",
        prix_eco: 4000,
        prix_business: 10000
    },
    bafoussam: {
        title: "Bafoussam",
        description: "ouest cameroun",
        prix_eco: 4000,
        prix_business: 10000
    },
    nord: {
        title: "Nord",
        description: "grand nord",
        prix_eco: 10000,
        prix_business: 20000
    },
    kribi: {
        title: "Kribi",
        description: "ville touristique",
        prix_eco: 5000,
        prix_business: 10000
    },
    est: {
        title: "Est",
        description: "ville historique",
        prix_eco: 5000,
        prix_business: 10000

}};

function openModal(destination)
{
    const modal= document.getElementById("modal");
    const title= document.getElementById("destination-title");
    const description= document.getElementById("destination-description");
    title.textContent= destinations[destination].title;
    description.textContent= destinations[destination].description;
    modal.style.display= "block";
}

function closeModal()
{
    document.getElementById("modal").style.display="none";
}