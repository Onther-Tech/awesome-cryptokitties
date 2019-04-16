
##################
Non Requestable Contracts
##################

.. contents:: Table Of Contents
  :depth: 5
---------

.. Template
.. 0. Struct
.. ---------

.. <Struct Name>
.. ^^^^^^^

.. Members
.. """""""
.. - ``<member name> <<type>>``: <description>

.. 1. Events
.. ---------
.. <Event Name>
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. <description>
.. Parameters
.. """""""""""
.. - ``<param name> <<type>>``: <description>

.. 2. External Functions
.. ------------

.. <Func Sig>
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. <description>

.. Parameters
.. """"""""""""
.. - ``<param name> <<type>>``: <description>

.. Returns
.. """"""""""""
.. ``<param name> <<type>>``: <description>

.. 3. Public State Variables
.. --------------------------
.. - ``<Variable Name> <<type>>``: <description>



.. _general-contracts:
********
General
********


ERC721
================

1. Events
---------

Transfer(address from, address to, uint256 tokenId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Approval(address owner, address approved, uint256 tokenId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


2. External Functions
------------

totalSupply() public view returns (uint256 total);
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameters
""""""""""""

Returns
""""""""""""

balanceOf(address _owner) public view returns (uint256 balance);
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameters
""""""""""""

Returns
""""""""""""

ownerOf(uint256 _tokenId) external view returns (address owner);
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameters
""""""""""""

Returns
""""""""""""

approve(address _to, uint256 _tokenId) external;
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameters
""""""""""""

Returns
""""""""""""

transfer(address _to, uint256 _tokenId) external;
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameters
""""""""""""

Returns
""""""""""""

transferFrom(address _from, address _to, uint256 _tokenId) external;
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameters
""""""""""""

Returns
""""""""""""
supportsInterface(bytes4 _interfaceID) external view returns (bool)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERC-165 Compatibility (https://github.com/ethereum/EIPs/issues/165)

Parameters
""""""""""""

Returns
""""""""""""


ERC721Metadata
==============

1. External Functions
---------------------

getMetadata(uint256 _tokenId, string) public view returns (bytes32[4] buffer, uint256 count)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameters
""""""""""

Returns
""""""""""""

--------

.. _auction-contracts:
********
Auctions
********


ClockAuctionBase
================

0. Struct
---------

Auction
^^^^^^^

Members
"""""""
- ``seller <address>``: Current owner of NFT
- ``startingPrice <uint128>``: Price (in wei) at beginning of auction
- ``endingPrice <uint128>``: Price (in wei) at end of auction
- ``duration <uint64>``: Duration (in seconds) of auction
- ``startedAt <uint64>``: Time when auction started

1. Events
---------

AuctionCreated(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

<description>

Parameters
"""""""""""
- ``tokenId <uint256>``:
- ``startingPrice <uint256>``:
- ``endingPrice <uint256>``:
- ``duration <uint256>``:

AuctionSuccessful(uint256 tokenId, uint256 totalPrice, address winner)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
<description>

Parameters
"""""""""""
- ``tokenId <uint256>``:
- ``totalPrice <uint256>``:
- ``winner <address>``:

AuctionCancelled(uint256 tokenId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

<description>

Parameters
"""""""""""

- ``tokenId <uint256>``: <description>


2. External Functions
---------------------

3. Public State Variables
--------------------------
- ``nonFungibleContract <ERC721>``: Reference to contract tracking NFT ownership
- ``ownerCut <uint256>``: Cut owner takes on each auction, measured in basis points (1/100 of a percent). Values 0-10,000 map to 0%-100%.


ClockAuction
============

1. Events
---------



2. External Functions
---------------------

.. <Func Sig>
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. <description>

.. Parameters
.. """"""""""""
.. - ``<param name> <<type>>``: <description>

.. Returns
.. """"""""""""
.. ``<param name> <<type>>``: <description>


withdrawBalance() external
^^^^^^^^^^^^^^^^^^^^^^^^^^
Remove all Ether from the contract, which is the owner's cuts as well as any Ether sent directly to the contract address. Always transfers to the NFT contract, but can be called either by the owner or the NFT contract.

Parameters
""""""""""""
None

Returns
""""""""""""
None


createAuction(uint256 _tokenId, uint256 _startingPrice, uint256 _endingPrice, uint256 _duration, address _seller) external whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates and begins a new auction.

Parameters
""""""""""""
- ``_tokenId <uint256>``: ID of token to auction, sender must be owner.
- ``_startingPrice <uint256>``: Price of item (in wei) at beginning of auction.
- ``_endingPrice <uint256>``: Price of item (in wei) at end of auction.
- ``_duration <uint256>``: Length of time to move between starting price and ending price (in seconds).
- ``_seller <address>``: Seller, if not the message sender

Returns
""""""""""""
None


bid(uint256 _tokenId) external payable whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Bids on an open auction, completing the auction and transferring ownership of the NFT if enough Ether is supplied.

Parameters
""""""""""""
- ``_tokenId <uint256>``: ID of token to bid on.

Returns
""""""""""""
None

cancelAuction(uint256 _tokenId) external
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Cancels an auction that hasn't been won yet. Returns the NFT to original owner.

Parameters
""""""""""""
- ``_tokenId <uint256>``: ID of token on auction.

Returns
""""""""""""
None



cancelAuctionWhenPaused(uint256 _tokenId) whenPaused onlyOwner external
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Cancels an auction when the contract is paused. Only the owner may do this, and NFTs are returned to the seller. This should only be used in emergencies.

Parameters
""""""""""""
- ``_tokenId <uint256>``: ID of the NFT on auction to cancel.

Returns
""""""""""""
None



getAuction(uint256 _tokenId) external view returns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns auction info for an NFT on auction.

Parameters
""""""""""""
- ``_tokenId <uint256>``: ID of NFT on auction.

Returns
""""""""""""
- ``seller <address>``:
- ``startingPrice <uint256>``:
- ``endingPrice <uint256>``:
- ``duration <uint256>``:
- ``startedAt <uint256>``:



getCurrentPrice(uint256 _tokenId) external view returns (uint256)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the current price of an auction.

Parameters
""""""""""""
- ``_tokenId <uint256>``: ID of the token price we are checking.

Returns
""""""""""""
- ``<uint256>``: Current price of an auction.



------------

.. _kitty-contracts:
********
Kitties
********


GeneScience
============

1. Events
---------

2. External Functions
---------------------


KittyAccessControl
============

1. Events
---------

2. External Functions
---------------------


KittyAuction
============

1. Events
---------

2. External Functions
---------------------


KittyBase
============

1. Events
---------

2. External Functions
---------------------


KittyBreeding
============

1. Events
---------

2. External Functions
---------------------


KittyCore
============

1. Events
---------

2. External Functions
---------------------


KittyMinting
============

1. Events
---------

2. External Functions
---------------------


KittyOwnership
============

1. Events
---------

2. External Functions
---------------------


