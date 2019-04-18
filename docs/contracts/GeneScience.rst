
GeneScience
===========

GeneScience implements the trait calculation for new kitties,


Constants
---------

- ``isGeneScience <bool>``



External Functions
------------------


decode(uint256 _genes) public pure returns(uint8[])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parse a kitten gene and returns all of 12 "trait stack" that makes the characteristics

Parameters
""""""""""

- ``_genes <uint256>``: kitten gene

Returns
"""""""

- ``<uint8[]>``: the 48 traits that composes the genetic code, logically divided in stacks of 4, where only the first trait of each stack may express

encode(uint8[] _traits) public pure returns (uint256 _genes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given an array of traits return the number that represent genes

Parameters
""""""""""

- ``_traits <uint8[]>``

Returns
"""""""

- ``_genes <uint256>``

expressingTraits(uint256 _genes) public pure returns(uint8[12])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

return the expressing traits

Parameters
""""""""""

- ``_genes <uint256>``: the long number expressing cat genes

Returns
"""""""

- ``<uint8[12]>``

mixGenes(uint256 _genes1, uint256 _genes2, uint256 _targetBlock) public returns (uint256)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the function as defined in the breeding contract - as defined in CK bible

Parameters
""""""""""

- ``_genes1 <uint256>``
- ``_genes2 <uint256>``
- ``_targetBlock <uint256>``

Returns
"""""""

- ``<uint256>``
