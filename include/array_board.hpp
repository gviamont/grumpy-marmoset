// Copyright 2021 The Knights of Ni

#pragma once

#include "constants.hpp"

namespace grumpy_marmoset {

class ArrayBoard {
 public:
    // Creates an array board with the chess pieces in the starting position.
    ArrayBoard();

    ~ArrayBoard() = default;
    ArrayBoard(const ArrayBoard &) = default;
    ArrayBoard &operator=(const ArrayBoard &ab) = default;

 private:
    Piece _board[kBoardSize];
};

}  // namespace grumpy_marmoset
