#!/usr/bin/env python3

from transmorph.datasets import load_test_datasets_small
from transmorph.engine.checking import NeighborEntropy
from transmorph.engine.matching import Labels
from transmorph.engine.merging import LinearCorrection
from transmorph.engine.traits import UsesReference
from transmorph.utils.anndata_manager import AnnDataKeyIdentifiers


def test_checking_neighborentropy():
    # Tests NeighborEntropy checking on a small dataset
    datasets = list(load_test_datasets_small().values())
    UsesReference.write_is_reference(datasets[1])
    matching = Labels(label_obs="class")
    matching.retrieve_all_labels(datasets)
    T = matching.fit([adata.X for adata in datasets])
    mg = LinearCorrection(n_neighbors=3)
    mg.retrieve_reference_index(datasets)
    mg.set_matchings(T)
    Xs_out = mg.transform(datasets, [adata.X for adata in datasets])
    check = NeighborEntropy(n_neighbors=5, threshold=0.29)
    assert check.check(Xs_out)


if __name__ == "__main__":
    test_checking_neighborentropy()
