<?php

namespace CustomRules;

use PhpParser\Node;
use PhpParser\Node\Stmt\ClassMethod;
use PHPStan\Analyser\Scope;
use PHPStan\Rules\Rule;
use PHPStan\Rules\RuleErrorBuilder;

class ExampleRule implements Rule
{
    public function getNodeType(): string
    {
        return ClassMethod::class;
    }

    public function processNode(Node $node, Scope $scope): array
    {
        if ($node->name->toString() === 'badMethod') {
            return [
                RuleErrorBuilder::message('Method name "badMethod" is forbidden.')->build(),
            ];
        }

        return [];
    }
}