#pragma once

#include "array_board.hpp"

#include <gtest/gtest.h>

namespace grumpy_marmoset {

class ArrayBoardTest : public ::testing::Test {
};

TEST_F(ArrayBoardTest, ConstructorWorks) {
    ArrayBoard ab;

    // Confirm white back rank.
    EXPECT_EQ(ab[Square::kA1], Piece::kWhiteRook);
    EXPECT_EQ(ab[Square::kB1], Piece::kWhiteKnight);
    EXPECT_EQ(ab[Square::kC1], Piece::kWhiteBishop);
    EXPECT_EQ(ab[Square::kD1], Piece::kWhiteQueen);
    EXPECT_EQ(ab[Square::kE1], Piece::kWhiteKing);
    EXPECT_EQ(ab[Square::kF1], Piece::kWhiteBishop);
    EXPECT_EQ(ab[Square::kG1], Piece::kWhiteKnight);
    EXPECT_EQ(ab[Square::kH1], Piece::kWhiteRook);

    // Confirm black back rank.
    EXPECT_EQ(ab[Square::kA8], Piece::kBlackRook);
    EXPECT_EQ(ab[Square::kB8], Piece::kBlackKnight);
    EXPECT_EQ(ab[Square::kC8], Piece::kBlackBishop);
    EXPECT_EQ(ab[Square::kD8], Piece::kBlackQueen);
    EXPECT_EQ(ab[Square::kE8], Piece::kBlackKing);
    EXPECT_EQ(ab[Square::kF8], Piece::kBlackBishop);
    EXPECT_EQ(ab[Square::kG8], Piece::kBlackKnight);
    EXPECT_EQ(ab[Square::kH8], Piece::kBlackRook);

    // Confirm pawns.
    for (int i = 0; i < 8; ++i) {
        EXPECT_EQ(ab[to_underlying(Square::kA2) + i], Piece::kWhitePawn);
        EXPECT_EQ(ab[to_underlying(Square::kA7) + i], Piece::kBlackPawn);
    }

    // Confirm empty space.
    for (int i = 0; i < 32; ++i) {
        EXPECT_EQ(ab[to_underlying(Square::kA3) + i], Piece::kEmpty);
    }
}

}  // namespace grumpy_marmoset
