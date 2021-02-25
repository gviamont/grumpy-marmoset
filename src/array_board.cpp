// Copyright 2021 The Knights of Ni

#include "array_board.hpp"

namespace grumpy_marmoset {

ArrayBoard::ArrayBoard() {
    // Initialize white back rank.
    _board[to_underlying(Square::kA1)] = Piece::kWhiteRook;
    _board[to_underlying(Square::kB1)] = Piece::kWhiteKnight;
    _board[to_underlying(Square::kC1)] = Piece::kWhiteBishop;
    _board[to_underlying(Square::kD1)] = Piece::kWhiteQueen;
    _board[to_underlying(Square::kE1)] = Piece::kWhiteKing;
    _board[to_underlying(Square::kF1)] = Piece::kWhiteBishop;
    _board[to_underlying(Square::kG1)] = Piece::kWhiteKnight;
    _board[to_underlying(Square::kH1)] = Piece::kWhiteRook;

    // Initialize black back rank.
    _board[to_underlying(Square::kA8)] = Piece::kBlackRook;
    _board[to_underlying(Square::kB8)] = Piece::kBlackKnight;
    _board[to_underlying(Square::kC8)] = Piece::kBlackBishop;
    _board[to_underlying(Square::kD8)] = Piece::kBlackQueen;
    _board[to_underlying(Square::kE8)] = Piece::kBlackKing;
    _board[to_underlying(Square::kF8)] = Piece::kBlackBishop;
    _board[to_underlying(Square::kG8)] = Piece::kBlackKnight;
    _board[to_underlying(Square::kH8)] = Piece::kBlackRook;

    for (int i = 0; i < 8; ++i) {
        _board[to_underlying(Square::kA2) + i] = Piece::kWhitePawn;
        _board[to_underlying(Square::kA7) + i] = Piece::kBlackPawn;
    }

    for (int i = 0; i < 32; ++i) {
        _board[to_underlying(Square::kA3) + i] = Piece::kEmpty;
    }
}

Piece
ArrayBoard::operator[](Square sq) const {
    return _board[to_underlying(sq)];
}

Piece
ArrayBoard::operator[](int sq) const {
    return _board[sq];
}

}  // namespace grumpy_marmoset
