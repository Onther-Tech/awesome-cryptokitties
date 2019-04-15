const KittyCore = artifacts.require("KittyCore");
const ERC721Metadata = artifacts.require("ERC721Metadata");
const GeneScience = artifacts.require("GeneScience");
const SaleClockAuction = artifacts.require("SaleClockAuction");
const SiringClockAuction = artifacts.require("SiringClockAuction");

module.exports = async function(deployer) {
  const fee = 100; // 1% auction fee

  await deployer.deploy(KittyCore);
  const kitty = await KittyCore.deployed();

  await deployer.deploy(ERC721Metadata);
  const erc721Metadata = await ERC721Metadata.deployed();

  await deployer.deploy(GeneScience);
  const geneScience = await GeneScience.deployed();

  await deployer.deploy(SaleClockAuction, kitty.address, fee);
  const saleClockAuction = await SaleClockAuction.deployed();

  await deployer.deploy(SiringClockAuction, kitty.address, fee);
  const siringClockAuction = await SiringClockAuction.deployed();

  await kitty.setSaleAuctionAddress(saleClockAuction.address);
  await kitty.setSiringAuctionAddress(siringClockAuction.address);
  await kitty.setMetadataAddress(erc721Metadata.address);
  await kitty.setGeneScienceAddress(geneScience.address);
};
