<?PHP
include_once("ARC/arc/ARC2.php");
include_once("ARC/Graphite.php");

$graph = new Graphite();
$graph -> ns("db", "http://dbpedia.org/resource/");
$graph -> ns("prop", "http://dbpedia.org/property/");
$graph -> ns("db-owl", "http://dbpedia.org/ontology/");

$graph -> load("db:Richard_Dawkins");

print $graph -> resource("db:Richard_Dawkins") -> dump();

?>
