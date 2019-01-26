# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['greenweez.com']
    start_urls = [
        'https://www.greenweez.com/aperitifs-bio-c1107?page=1',
        'https://www.greenweez.com/superaliments-superfruits-c3245?page=1',
        'https://www.greenweez.com/thes-bio-et-infusions-c611?page=1',
        'https://www.greenweez.com/format-familial-economique-vrac-c3962?page=1',
        'https://www.greenweez.com/cuisine-du-monde-bio-c5453?page=1',
        'https://www.greenweez.com/selection-produits-veggie-celnat-c5117?page=1',
        'https://www.greenweez.com/boissons-vegetales-c1421?page=1',
        'https://www.greenweez.com/Jus-de-fruits-bio-c1324?page=1',
        'https://www.greenweez.com/jus-de-legumes-c3314?page=1',
        'https://www.greenweez.com/sodas-bio-c3271?page=1',
        'https://www.greenweez.com/vins-bio-c3269?page=1',
        'https://www.greenweez.com/bieres-bio-c1768?page=1',
        'https://www.greenweez.com/Alcools-bio-c4705?page=1',
        'https://www.greenweez.com/boisson-bien-etre-c5347?page=1',
        'https://www.greenweez.com/jus-de-grenade-c2295?page=1',
        'https://www.greenweez.com/sirops-bio-c1325?page=1',
        'https://www.greenweez.com/eau-de-coco-c3994?page=1',
        'https://www.greenweez.com/thes-glaces-c4678?page=1',
        'https://www.greenweez.com/eaux-aromatisees-bio-c5651?page=1',
        'https://www.greenweez.com/Lait-de-vache-et-chevre-c2638?page=1',
        'https://www.greenweez.com/epicerie-sans-gluten-c751?page=1',
        'https://www.greenweez.com/produits-vegetarien-vegan-bio-c987?page=1',
        'https://www.greenweez.com/poisson-viande-bio-c2182?page=1',
        'https://www.greenweez.com/petit-dejeuner-bio-c3279?page=1',
        'https://www.greenweez.com/legumes-et-plats-cuisines-bio-c746?page=1',
        'https://www.greenweez.com/huiles-alimentaires-bio-c1410?page=1',
        'https://www.greenweez.com/fruits-secs-et-purees-c1103?page=1',
        'https://www.greenweez.com/farines-bio-c743?page=1',
        'https://www.greenweez.com/epicerie-bio-sucree-c1060?page=1',
        'https://www.greenweez.com/condiments-aides-culinaires-c749?page=1',
        'https://www.greenweez.com/cereales-graines-bio-c736?page=1',
        'https://www.greenweez.com/boissons-vegetales-c1421?page=1',
        'https://www.greenweez.com/produits-frais-vegan-bio-c4055?page=1',
        'https://www.greenweez.com/fruits-et-legumes-bio-c4602?page=1',
        'https://www.greenweez.com/boulangerie-fraiche-c4166?page=1',
        'https://www.greenweez.com/boissons-fraiches-c4167?page=1',
        'https://www.greenweez.com/riz-pates-cereales-rayon-frais-c5211?page=1',
        'https://www.greenweez.com/conserves-du-rayon-frais-c5209?page=1',
        'https://www.greenweez.com/sauces-et-condiments-rayon-frais-c5208?page=1',
        'https://www.greenweez.com/epicerie-sucree-du-rayon-frais-c5210?page=1',
        'https://www.greenweez.com/repas-festif-c5115?page=1',
        'https://www.greenweez.com/promotion-dlc-courte-c4897?page=1',
        'https://www.greenweez.com/prix-engages-c4697?page=1',
        'https://www.greenweez.com/gros-conditionnements-pros-c4826?page=1',
        'https://www.greenweez.com/Poissonnerie-et-boucherie-c4060?page=1',
        'https://www.greenweez.com/charcuteries-bio-c4051?page=1',
        'https://www.greenweez.com/cremerie-c4042?page=1',
        'https://www.greenweez.com/charcuteries-bio-c4051?page=1',
        'https://www.greenweez.com/cremerie-c4042?page=1',
        'https://www.greenweez.com/fromages-bio-c4046?page=1',
        'https://www.greenweez.com/yaourts-et-desserts-bio-c4775?page=1',
        'https://www.greenweez.com/traiteur-c4050?page=1',
        'https://www.greenweez.com/desserts-lactes-bio-bebe-c2691?page=1',
        'https://www.greenweez.com/gouters-biscuits-bio-bebe-c1302?page=1',
        'https://www.greenweez.com/bouillies-bio-bebe-c881?page=1',
        'https://www.greenweez.com/cereales-bio-bebe-c633?page=1',
        'https://www.greenweez.com/huiles-bebe-bio-c3713?page=1',
        'https://www.greenweez.com/boissons-bebe-bio-c632?page=1',
        'https://www.greenweez.com/alimentation-enfants-bio-c3222?page=1',
        'https://www.greenweez.com/alimentation-bebe-sans-gluten-c3180?page=1',
        'https://www.greenweez.com/soupes-bio-bebe-c1303?page=1',
        'https://www.greenweez.com/petits-pots-bebe-du-soir-c2978?page=1',
        'https://www.greenweez.com/petits-pots-fruits-bebe-c2962?page=1',
        'https://www.greenweez.com/petits-pots-legumes-bebe-c2998?page=1',
        'https://www.greenweez.com/petits-pots-bebe-du-midi-c2971?page=1',
        'https://www.greenweez.com/preparations-vegetales-bebe-c2923?page=1',
        'https://www.greenweez.com/preparation-bio-au-lait-de-brebis-c2994?page=1',
        'https://www.greenweez.com/preparations-au-lait-de-chevre-bio-bebe-c2925?page=1',
        'https://www.greenweez.com/lait-infantile-bio-c631?page=1',
        'https://www.greenweez.com/soins-solaires-c49?page=1',
        'https://www.greenweez.com/hygiene-bebe-soin-maternite-c3030?page=1',
        'https://www.greenweez.com/couche-ecologique-c3012?page=1',
        'https://www.greenweez.com/soins-a-l-aloe-vera-c4810?page=1',
        'https://www.greenweez.com/argile-c1089?page=1',
        'https://www.greenweez.com/cosmetique-grand-format-c4913?page=1',
        'https://www.greenweez.com/cosmetique-vegan-c4716?page=1',
        'https://www.greenweez.com/cosmetique-ayurvedique-c3256?page=1',
        'https://www.greenweez.com/cosmetiques-a-faire-soi-meme-c2169?page=1',
        'https://www.greenweez.com/coffrets-cadeaux-c5204?page=1',
        'https://www.greenweez.com/soins-homme-c427?page=1',
        'https://www.greenweez.com/soins-du-corps-c101?page=1',
        'https://www.greenweez.com/soins-du-visage-c52?page=1',
        'https://www.greenweez.com/maquillage-c144?page=1',
        'https://www.greenweez.com/epilation-c1408?page=1',
        'https://www.greenweez.com/soins-des-cheveux-c85?page=1',
        'https://www.greenweez.com/douche-et-bain-c44?page=1',
        'https://www.greenweez.com/hygiene-c70?page=1',
        'https://www.greenweez.com/livres-maternite-education-c5821?page=1',
        'https://www.greenweez.com/fournitures-scolaires-c416?page=1',
        'https://www.greenweez.com/bracelet-collier-ambre-bebe-c816?page=1',
        'https://www.greenweez.com/linge-de-lit-bebe-enfant-c996?page=1',
        'https://www.greenweez.com/matelas-bebe-enfant-c638?page=1',
        'https://www.greenweez.com/chambre-et-mobilier-enfant-c521?page=1',
        'https://www.greenweez.com/transport-enfant-c1230?page=1',
        'https://www.greenweez.com/loisirs-creatifs-c1592?page=1',
        'https://www.greenweez.com/veilleuses-reveils-c51?page=1',
        'https://www.greenweez.com/jouets-sains-c40?page=1',
        'https://www.greenweez.com/chaussons-bebes-c2709?page=1',
        'https://www.greenweez.com/vetements-accessoires-c54?page=1',
        'https://www.greenweez.com/hygiene-soins-c96?page=1',
        'https://www.greenweez.com/couches-ecologiques-c74?page=1',
        'https://www.greenweez.com/allaitement-c2131?page=1',
        'https://www.greenweez.com/biberons-accessoires-c80?page=1',
        'https://www.greenweez.com/le-repas-de-bebe-c58?page=1',
        'https://www.greenweez.com/alimentation-bebe-c2108?page=1',
        'https://www.greenweez.com/entretien-des-wc-c785?page=1',
        'https://www.greenweez.com/desodorisants-c791?page=1',
        'https://www.greenweez.com/anti-insecte-c1205?page=1',
        'https://www.greenweez.com/anti-calcaire-c795?page=1',
        'https://www.greenweez.com/produits-nettoyants-pour-vitres-c786?page=1',
        'https://www.greenweez.com/accessoires-menagers-c3725?page=1',
        'https://www.greenweez.com/impermeabilisants-c1204?page=1',
        'https://www.greenweez.com/nettoyants-techniques-ecologiques-c796?page=1',
        'https://www.greenweez.com/Savon-noir-maison-c2368?page=1',
        'https://www.greenweez.com/nettoyants-multi-usages-c797?page=1',
        'https://www.greenweez.com/produits-vaisselle-c787?page=1',
        'https://www.greenweez.com/soin-du-linge-c3723?page=1',
        'https://www.greenweez.com/Savon-de-Marseille-Linge-c2367?page=1',
        'https://www.greenweez.com/lessives-ecologiques-c790?page=1',
        'https://www.greenweez.com/droguerie-ecologique-c3635?page=1',
        'https://www.greenweez.com/les-indispensables-c5229?page=1',
        'https://www.greenweez.com/materiel-medical-c2527?page=1',
        'https://www.greenweez.com/massage-kinesitherapie-c926?page=1',
        'https://www.greenweez.com/relaxation-detente-sommeil-c2459?page=1',
        'https://www.greenweez.com/sport-et-nutrition-c873?page=1',
        'https://www.greenweez.com/luminotherapie-c854?page=1',
        'https://www.greenweez.com/diffuseurs-d-huiles-essentielles-c1316?page=1',
        'https://www.greenweez.com/aromatherapie-c3642?page=1',
        'https://www.greenweez.com/digestion-transit-flore-c589?page=1',
        'https://www.greenweez.com/minceur-c601?page=1',
        'https://www.greenweez.com/parapharmacie-c2526?page=1',
        'https://www.greenweez.com/fleurs-de-bach-phytotherapie-elixirs-floraux-c595?page=1',
        'https://www.greenweez.com/phytotherapie-c3428?page=1',
        'https://www.greenweez.com/vitamines-mineraux-c2468?page=1',
        'https://www.greenweez.com/nez-gorge-oreille-c594?page=1',
        'https://www.greenweez.com/resistance-et-vitalite-c590?page=1',
        'https://www.greenweez.com/complements-alimentaires-c2522?page=1',
        'https://www.greenweez.com/zero-dechet-c5397?page=1',
        'https://www.greenweez.com/livres-vie-saine-c1330?page=1',
        'https://www.greenweez.com/mode-bio-c1491?page=1',
        'https://www.greenweez.com/appareils-de-mesure-c99?page=1',
        'https://www.greenweez.com/energie-c2972?page=1',
        'https://www.greenweez.com/Soldes-cosmetiques-c1356?page=1',
        'https://www.greenweez.com/soldes-cuisine-c1353?page=1',
        'https://www.greenweez.com/Soldes-enfant-c1351?page=1',
        'https://www.greenweez.com/Soldes-epicerie-c1352?page=1',
        'https://www.greenweez.com/Soldes-maison-c1349?page=1',
        'https://www.greenweez.com/Soldes-sante-c1355?page=1',
        'https://www.greenweez.com/rangement-c2284?page=1',
        'https://www.greenweez.com/peinture-bricolage-c1407?page=1',
        'https://www.greenweez.com/transport-ecologique-c30?page=1',
        'https://www.greenweez.com/traitement-de-l-eau-c27?page=1',
        'https://www.greenweez.com/traitement-de-l-air-c26?page=1',
        'https://www.greenweez.com/detecteur-anti-ondes-c55?page=1',
        'https://www.greenweez.com/lumiere-c25?page=1',
        'https://www.greenweez.com/decoration-c79?page=1',
        'https://www.greenweez.com/salle-de-bains-c81?page=1',
        'https://www.greenweez.com/chambre-c65?page=1',
        'https://www.greenweez.com/nature-activites-d-exterieur-c72?page=1',
        'https://www.greenweez.com/mobilier-exterieur-piscine-c1131?page=1',
        'https://www.greenweez.com/jardin-c92?page=1',
        'https://www.greenweez.com/animalerie-bio-c5150?page=1',
        'https://www.greenweez.com/livres-cuisine-c4746?page=1',
        'https://www.greenweez.com/cuisine-vegan-c4898?page=1',
        'https://www.greenweez.com/composteurs-et-poubelles-de-tri-c1882?page=1',
        'https://www.greenweez.com/chariots-de-courses-c1339?page=1',
        'https://www.greenweez.com/pour-emporter-c992?page=1',
        'https://www.greenweez.com/ustensiles-de-cuisine-c698?page=1',
        'https://www.greenweez.com/carafes-et-fontaines-c1288?page=1',
        'https://www.greenweez.com/conservation-c831?page=1',
        'https://www.greenweez.com/cuisson-vapeur-c702?page=1',
        'https://www.greenweez.com/cocottes-plat-a-four-c2171?page=1',
        'https://www.greenweez.com/poeles-sauteuses-c705?page=1',
        'https://www.greenweez.com/casseroles-faitouts-c706?page=1',
        'https://www.greenweez.com/germoirs-c700?page=1',
        'https://www.greenweez.com/deshydrateurs-alimentaires-c704?page=1',
        'https://www.greenweez.com/extracteurs-de-jus-c731?page=1',
        'https://www.greenweez.com/appareils-de-cuisine-c730?page=1'
    ]

    def parse(self, response):
        urls = response.xpath('//div[@class="rayon_img"]/div[@class="titre"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.individual_page)

        # Calling next page
        for page in range(2, 10):
            next_page_url = str(response.url.split('=')[0]) + "=" + str(page)
            yield scrapy.Request(url=next_page_url)

    def individual_page(self, response):
        fields = dict()
        fields["base_price"] = response.xpath('//div[@class="prix_barre"]/text()').re_first('(\d+\,\d+)')
        fields["discounted_price"] = response.xpath('//div[@class="fp_price_tag"]/text()').re_first('(\d+\,\d+)')
        fields["product_name"] = response.xpath('//h1/span/text()').extract_first()
        fields["category"] = response.xpath('//div[@class="fil_ariane_txt"]/ul/li/a[@class="fleche_souligne"]/span/text()').extract()
        fields["brand"] = response.xpath('//h1/a/text()').extract_first()
        fields["description"] = response.xpath('//div[@class="fp_txt"]/span/p/text()').extract_first()

        yield fields