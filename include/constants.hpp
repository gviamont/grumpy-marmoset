// Copyright 2021 The Knights of Ni

#pragma once

#include <cstdint>
#include <type_traits>
#include <typeinfo>

namespace grumpy_marmoset {

static constexpr int kBoardSize = 64;

template< typename E >
constexpr typename std::underlying_type<E>::type to_underlying(E e) {
    return static_cast<typename std::underlying_type<E>::type>(e);
}

enum class Piece : uint8_t {
    kEmpty = 0,
    kWhitePawn = 1,
    kWhiteKnight = 2,
    kWhiteBishop = 3,
    kWhiteRook = 4,
    kWhiteQueen = 5,
    kWhiteKing = 6,
    kBlackPawn = 7,
    kBlackKnight = 8,
    kBlackBishop = 9,
    kBlackRook = 10,
    kBlackQueen = 11,
    kBlackKing = 12
};

enum class Square : uint8_t {
    kA1 = 0,
    kB1 = 1,
    kC1 = 2,
    kD1 = 3,
    kE1 = 4,
    kF1 = 5,
    kG1 = 6,
    kH1 = 7,
    kA2 = 8,
    kB2 = 9,
    kC2 = 10,
    kD2 = 11,
    kE2 = 12,
    kF2 = 13,
    kG2 = 14,
    kH2 = 15,
    kA3 = 16,
    kB3 = 17,
    kC3 = 18,
    kD3 = 19,
    kE3 = 20,
    kF3 = 21,
    kG3 = 22,
    kH3 = 23,
    kA4 = 24,
    kB4 = 25,
    kC4 = 26,
    kD4 = 27,
    kE4 = 28,
    kF4 = 29,
    kG4 = 30,
    kH4 = 31,
    kA5 = 32,
    kB5 = 33,
    kC5 = 34,
    kD5 = 35,
    kE5 = 36,
    kF5 = 37,
    kG5 = 38,
    kH5 = 39,
    kA6 = 40,
    kB6 = 41,
    kC6 = 42,
    kD6 = 43,
    kE6 = 44,
    kF6 = 45,
    kG6 = 46,
    kH6 = 47,
    kA7 = 48,
    kB7 = 49,
    kC7 = 50,
    kD7 = 51,
    kE7 = 52,
    kF7 = 53,
    kG7 = 54,
    kH7 = 55,
    kA8 = 56,
    kB8 = 57,
    kC8 = 58,
    kD8 = 59,
    kE8 = 60,
    kF8 = 61,
    kG8 = 62,
    kH8 = 63
};

}  // namespace grumpy_marmoset
